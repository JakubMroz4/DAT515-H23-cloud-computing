from sqlalchemy import ForeignKey

from app import db, ma
import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    author = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=False)

    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.date_posted = (str(datetime.date.today().year) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().day) + " "
        + str(datetime.datetime.now().hour)) + ":" + str(datetime.datetime.now().minute)


class PostSchema(ma.Schema):
    class Meta:
        fields = ('id','author','text','date_posted')
