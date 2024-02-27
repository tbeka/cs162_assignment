from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, List, Item
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Route to display all todo lists
@main.route('/todo')
@login_required
def todo():
    user_lists = List.query.filter_by(user_id=current_user.id).all()
    return render_template('todo.html', lists=user_lists)

# Route to add a new list (GET to display form, POST to submit form)
@main.route('/todo/add-list', methods=['GET', 'POST'])
@login_required
def add_list():
    if request.method == 'POST':
        list_title = request.form.get('title')
        if not list_title:
            flash('List title is required.', 'error')
            return redirect(url_for('main.add_list'))
        new_list = List(title=list_title, user_id=current_user.id)
        db.session.add(new_list)
        db.session.commit()
        flash('List added successfully!', 'success')
        return redirect(url_for('main.todo'))
    return render_template('add_list.html')  # You'll need to create this template

#TODO: add more routes.

#expanding one task and seeing its subtasks
#adding list
#adding a task
#deletinga a list
#deleting a task