"""Models for Blogly."""
import datetime
from time import timezone
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    """Connect to database; call this function in app.py"""
    db.app = app
    db.init_app(app)

#models come down here

class User(db.Model):
    """User"""
    __tablename__="users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    first_name = db.Column(db.String(20), nullable = False)

    last_name = db.Column(db.String(20), nullable = False)

    image_url = db.Column(db.String(2048), nullable = False, default = 'https://pbs.twimg.com/profile_images/1237550450/mstom.jpg')

    posts = db.relationship('Post', backref = 'user', cascade='all, delete')

    def __repr__(self):
        u=self
        return F"<Name: {u.first_name} {u.last_name}>"

    def get_full_name(self):
        return F"{self.first_name} {self.last_name}" 

    

class Post(db.Model):
    """A post by a User"""
    __tablename__="posts"

    @property
    def date(self):
        dt = self.created_at
        date = dt.strftime('%A, %d. %B %Y %I:%M%p')
        return date

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    title = db.Column(db.String(100), nullable = False)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    categories = db.relationship('PostTag', backref = 'posts', cascade='all, delete')


class PostTag(db.Model):
    """Mapping tags to Posts"""
    __tablename__='posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


class Tag(db.Model):
    """A tag for Posts"""
    __tablename__='tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tag_name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship('Post', secondary="posts_tags", backref="tags")


