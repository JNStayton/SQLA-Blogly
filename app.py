"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecret'

connect_db(app)
db.create_all()


@app.route('/')
def go_home():
    """redirects to the home page"""
    return redirect('/users')

@app.route('/users')
def show_homepage():
    """Shows homepage index.html, with most recent posts and the list of all users"""
    users = User.query.all()
    posts = Post.query.order_by('created_at').limit(5).all()
    return render_template('index.html', users=users, posts=posts)

@app.route('/users/new') 
def sign_up():
    """Display form for users to register"""
    return render_template('newuser.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    """Creates a new user and saves to the db"""
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    image_url=request.form['image_url'] if request.form['image_url'] else None

    new_user=User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about the user"""
    user=User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Edit details about the user"""
    user=User.query.get_or_404(user_id)
    return render_template('edituser.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def save_edited_user(user_id):
    """Saves edited user details to DB"""
    user=User.query.get_or_404(user_id)

    user.first_name=request.form['first_name']
    user.last_name=request.form['last_name']
    user.image_url=request.form['image_url']
    
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Deletes user from DB"""
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    """Show the form to add a new post"""
    user=User.query.get_or_404(user_id)
    return render_template('newpost.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def create_post(user_id):
    """Creates the post, saves it to the DB"""
    user=User.query.get_or_404(user_id)

    title=request.form['title']
    content=request.form['content']

    new_post = Post(title=title, content=content, user_id=user.id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Shows the post details"""
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show the form to edit post details"""
    post=Post.query.get_or_404(post_id)
    return render_template('editpost.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def save_edited_post(post_id):
    """Saves edited post details to the DB"""
    post=Post.query.get_or_404(post_id)

    post.title=request.form['title']
    post.content=request.form['content']
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Deletes post from the DB"""
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect('/users')