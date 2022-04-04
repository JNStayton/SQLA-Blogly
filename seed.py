"""Seed file to make data for users table in blogly db"""

from ipaddress import _BaseNetwork
from models import User, Post, Tag, PostTag, db 
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

maru = User(first_name='Maru', last_name='the Cat', image_url='https://texashillcountry.com/wp-content/uploads/marucat-660x400.jpg')

# Add new objects to session, so they'll persist
db.session.add_all([jareth, alan, daryl, maru])

#commit--otherwise, this never gets saved!
db.session.commit()

# Add posts
mrow = Post(title='Mrrow', content='Brrrrrp mrrrrrrrow mew mewww', user_id=4)
herds = Post(title='This just in...', content='They do move in herds.', user_id=2)
babe = Post(title='What babe?', content='The babe with the power.', user_id=1)

db.session.add_all([mrow, herds, babe])
db.session.commit()

# Add tags
fun = Tag(tag_name='Fun')
wow = Tag(tag_name='Wow')
baw = Tag(tag_name='BAWW!')

db.session.add_all([fun, wow, baw])
db.session.commit()

# Map Tags to Posts
mrow.categories.append(PostTag(post_id=1, tag_id=1))
mrow.categories.append(PostTag(post_id=1, tag_id=3))
herds.categories.append(PostTag(post_id=2, tag_id=2))
babe.categories.append(PostTag(post_id=3, tag_id=1))
babe.categories.append(PostTag(post_id=3, tag_id=2))

db.session.add_all([mrow, herds, babe])
db.session.commit()







