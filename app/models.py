from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime

class Quote():

    def __init__(self,id,author,quote):
        self.id = id
        self.author = author
        self.quote = quote

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(1000))
    pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref='user',lazy="dynamic")
    comments = db.relationship('Comments',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def get_token(self, expiration=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'user':self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        id = data.get('user')
        if id:
            return User.query.get(id)
        return None

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key=True)
    blog_title = db.Column(db.String(255))
    blog_content = db.Column(db.String(1000))
    category = db.Column(db.String())
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref='review',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    @classmethod
    def get_all_blogs(cls):
        blog = Blog.query.all()
        return blogs

    @classmethod
    def get_users_blogs(cls,uname):
        user = User.query.filter_by(username=uname).first()
        user_blogs = Blog.query.filter_by(user_id=user.id).all()
        return user_blogs

    def __repr__(self):
        return f'Blog {self.blog_title}'

class Comments(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    blog = db.Column(db.Integer,db.ForeignKey("blog.id"))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog):
        comments = Comments.query.filter_by(blog=blog.id).all()
        return comments