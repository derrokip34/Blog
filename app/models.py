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

