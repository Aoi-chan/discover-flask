from app import db, bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):

    __tablename__ = "posts"
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id   = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<{}>'.format(self.title)

class Users(db.Model):

    __tablename__ = "users"

    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    pw    = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = bcrypt.generate_password_hash(pw)

