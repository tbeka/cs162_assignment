from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('index.html')

#TODO: add more routes.

#expanding one task and seeing its subtasks
#adding list
#adding a task
#deletinga a list
#deleting a task