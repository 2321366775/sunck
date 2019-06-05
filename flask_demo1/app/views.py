from app import app,db,lm,oid
from flask import render_template,redirect,flash,session,url_for,request,g
from flask_login import login_user, logout_user, current_user, login_required
from app import lm
from .models import User

@app.route('/index')
def index():
    users = User.query.all()
    for user in users:
        print(user.name)
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

from .forms import LoginFrom
@app.route('/login',methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginFrom()
    if form.validate_on_submit():
        session['remeber_me'] = form.remember_me.data
        # oid.try_login 被调用是为了触发用户使用 Flask-OpenID 认证。该函数有两个参数
        # OpenID 认证异步发生。如果认证成功的话，Flask-OpenID 将会调用一个注册了
        # oid.after_login 装饰器的函数。如果失败的话，用户将会回到登陆页面。
        return oid.try_login(form.openid.data,ask_for=['nicename','email'])
    # if form.validate_on_submit():
    #     session['remember_me'] = form.remember_me.data
    #     flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
    #     return redirect('/index')
    return render_template('login.html',Title = 'Sign In',form = form)

# 编写一个函数用于从数据库加载用户。这个函数将会被 Flask-Login
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


