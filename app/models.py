from . import db

class Quote():

    def __init__(self,id,author,quote):
        self.id = id
        self.author = author
        self.quote = quote

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(1000))
    pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref='user',lazy="dynamic")
    comments = db.relationship('Comments',backref='review',lazy='dynamic')


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key=True)
    blog_title = db.Column(db.String(255))
    blog_content = db.Column(db.String(1000))
    category = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref='review',lazy='dynamic')

class Comments(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    blog = db.Column(db.Integer,db.ForeignKey("blog.id"))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))