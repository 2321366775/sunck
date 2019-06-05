from app import db


# class Role(db.Model):
#
#     __tablename__ = "roles"
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(16),unique=True)
#     # 给Role类创建一个uses属性，关联users表。
#     # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
#     users = db.relationship('User',backref="role")
#     # 相当于__str__方法。
#     def __repr__(self):
#         return "Role: %s %s" % (self.id,self.name)
#
#
# class User(db.Model):
#     # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
#     __tablename__ = "users"
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(16),unique=True)
#     email = db.Column(db.String(32),unique=True)
#     password = db.Column(db.String(16))
#     # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
#     role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         try:
#             return str(self.id)
#         except NameError:
#             return str(self.id)  # python 3
#
#     def __repr__(self):
#         return "User: %s %s %s %s" % (self.id,self.name,self.password,self.role_id)
# '''
# 两张表
# 角色（管理员、普通用户）
# 用户（角色id)
#
# '''
class User(db.Model):
    # __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)