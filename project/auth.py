from flask import Blueprint, flash, render_template, redirect, url_for, request
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)

# Login form
@auth.route('/login')
def login():
    return render_template('auth_pages/login.html')

# Handling login form submission
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Check if the user exists and password matches
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # Reload login page if login fails

    # If login successful, log the user in
    login_user(user, remember=remember)
    return redirect(url_for('main.todo'))

# Signup form
@auth.route('/signup')
def signup():
    return render_template('auth_pages/signup.html')

# Handling signup form submission
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # Check if email already exists
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # Create a new user with hashed password
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

# Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))