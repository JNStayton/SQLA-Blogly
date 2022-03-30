"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User

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
    """Shows homepage index.html, with list of all users"""
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/new') 
def sign_up():
    """Display form for users to register"""
    return render_template('new.html')

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
    return render_template('details.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user=User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def save_edited_user(user_id):
    user=User.query.get_or_404(user_id)

    user.first_name=request.form['first_name']
    user.last_name=request.form['last_name']
    user.image_url=request.form['image_url']
    
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/users')

