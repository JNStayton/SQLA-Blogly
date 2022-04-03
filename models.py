"""Models for Blogly."""
from time import timezone
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
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

    def __repr__(self):
        u=self
        return F"<Name: {u.first_name} {u.last_name}>"

    def get_full_name(self):
        return F"{self.first_name} {self.last_name}" 

    

class Post(db.Model):
    """A post by a User"""
    __tablename__="posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    title = db.Column(db.String(100), nullable = False)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref = 'posts')