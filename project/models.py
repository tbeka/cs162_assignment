from . import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)  
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # One-to-many relationship with List model, representing todo lists owned by the user
    lists = db.relationship('List', backref='user', lazy=True)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # Foreign key referencing the id of the user who owns this list
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # One-to-many relationship with Item model, representing tasks within this todo list
    items = db.relationship('Item', backref='list', lazy=True, cascade="all, delete-orphan")

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    
    # Foreign key referencing the id of the parent task, can be null
    parent_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)
    
    # One-to-many relationship with itself, representing subtasks of this task
    children = db.relationship('Item', 
                               backref=db.backref('parent', remote_side=[id]), 
                               lazy=True, 
                               cascade="all, delete-orphan") # Delete subtasks when parent task is deleted
    
    # Boolean flag indicating whether the task is collapsed (hidden) in UI by default
    is_collapsed = db.Column(db.Boolean, default=False)