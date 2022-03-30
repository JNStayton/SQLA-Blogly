"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

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
