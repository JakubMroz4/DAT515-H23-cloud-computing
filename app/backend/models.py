from sqlalchemy import ForeignKey

from app import db, ma
import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    author = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=False)

    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.date_posted = (str(datetime.date.today().year) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().day))


class PostSchema(ma.Schema):
    class Meta:
        fields = ('id','author','text','date_posted')

class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(400), nullable=False)

    def __init__(self, email):
        self.email = email