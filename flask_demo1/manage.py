from app import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app.models import Post,User
manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)


if __name__ == '__main__':
    # ro1 = Role(name='admin')
    # # 先将ro1对象添加到会话中，可以回滚。
    # db.session.add(ro1)
    #
    # ro2 = Role()
    # ro2.name = 'user'
    # db.session.add(ro2)
    # # 最后插入完数据一定要提交
    # db.session.commit()
    #
    # us1 = User(nickname='wang', email='wang@163.com')
    # us2 = User(nickname='zhang', email='zhang@189.com')
    # us3 = User(nickname='chen', email='chen@126.com')
    # us4 = User(nickname='zhou', email='zhou@163.com')
    # us5 = User(nickname='tang', email='tang@itheima.com')
    # us6 = User(nickname='wu', email='wu@gmail.com')
    # us7 = User(nickname='qian', email='qian@gmail.com')
    # us8 = User(nickname='liu', email='liu@itheima.com')
    # us9 = User(nickname='li', email='li@163.com')
    # us10 = User(nickname='sun', email='sun@163.com')
    # db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    # db.session.commit()

    manage.run()
    # app.run(debug=True)