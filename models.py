from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # In a real app, ensure passwords are hashed
    lists = db.relationship('List', backref='user', lazy=True)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('Item', backref='list', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)
    children = db.relationship('Item', backref=db.backref('parent', remote_side=[id]), lazy=True)
    is_complete = db.Column(db.Boolean, default=False)
    is_collapsed = db.Column(db.Boolean, default=False)