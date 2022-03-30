"""Seed file to make data for users table in blogly db"""

from models import User, db 
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users

jareth = User(first_name='Jareth', last_name='the Goblin King', image_url='https://www.denofgeek.com/wp-content/uploads/2021/09/David-Bowie-Jareth-Labyrinth.jpg?resize=768%2C432')

alan = User(first_name='Alan', last_name='Grant', image_url='https://cdn.mos.cms.futurecdn.net/odZSGvFMc64sfWRS6NTXsa.jpg')

daryl = User(first_name='Daryl', last_name='Dixon', image_url='https://www.popmythology.com/wp-content/uploads/2013/11/Daryl-Dixon-Walking-Dead.jpg')

# Add new objects to session, so they'll persist
db.session.add(jareth)
db.session.add(alan)
db.session.add(daryl)

#commit--otherwise, this never gets saved!
db.session.commit()
