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
    return render_template('todo.html', name=current_user.name, lists=user_lists)

# Add a new list
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

# Delete a list
@main.route('/todo/delete-list/<int:list_id>', methods=['POST'])
@login_required
def delete_list(list_id):
    list_to_delete = List.query.get_or_404(list_id)
    if list_to_delete.user_id != current_user.id:
        flash('Unauthorized to delete this list.', 'error')
        return redirect(url_for('main.todo'))
    db.session.delete(list_to_delete)
    db.session.commit()
    flash('List deleted successfully!', 'success')
    return redirect(url_for('main.todo'))

@main.route('/todo/add-task/<int:list_id>', methods=['POST'])
@login_required
def add_task(list_id):
    content = request.form.get('taskContent')
    parent_id = request.form.get('parent_id', None)  # Get parent_id, default to None if not provided

    if content:
        # Create a new item with the content, list_id, and optional parent_id
        new_item = Item(content=content, list_id=list_id, parent_id=parent_id)
        db.session.add(new_item)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task content is required.', 'error')
    
    return redirect(url_for('main.todo'))



@main.route('/update-list-title/<int:list_id>', methods=['POST'])
@login_required
def update_list_title(list_id):
    list_to_update = List.query.get_or_404(list_id)
    if list_to_update.user_id != current_user.id:
        flash('Unauthorized action.', 'error')
        return redirect(url_for('main.todo'))
    
    new_title = request.form.get('new_title')
    if not new_title:
        flash('A new title is required.', 'error')
        return redirect(url_for('main.todo'))
    
    list_to_update.title = new_title
    db.session.commit()
    flash('List title updated successfully.', 'success')
    return redirect(url_for('main.todo'))

@main.route('/todo/update-task/<int:item_id>', methods=['POST'])
@login_required
def update_task(item_id):
    item = Item.query.get_or_404(item_id)
    if item.list.user_id != current_user.id:
        flash('Unauthorized action.', 'error')
        return redirect(url_for('main.todo'))

    new_content = request.form.get('new_content')
    if not new_content:
        flash('Task content is required.', 'error')
        return redirect(url_for('main.todo'))

    item.content = new_content
    db.session.commit()
    flash('Task updated successfully!', 'success')
    return redirect(url_for('main.todo'))

@main.route('/todo/delete-task/<int:item_id>', methods=['POST'])
@login_required
def delete_task(item_id):
    item = Item.query.get_or_404(item_id)
    if item.list.user_id != current_user.id:
        flash('Unauthorized action.', 'error')
        return redirect(url_for('main.todo'))

    db.session.delete(item)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.todo'))



#TASKS:
# Add the ability to rename with a nice edit icon
# Add the ability to delete with a nice X icon
# Add the ability to move between lists 
# Add the ability to add subtasks
# Add the ability to expand and collapse subtasks
# Add the ability to add sub-subtasks
# Add the ability to expand and collapse sub-subtasks