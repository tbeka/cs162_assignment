
# Hierarchical Todo List App

The Hierarchical Todo List App is a web application designed to help users manage their tasks in a structured and intuitive manner. Featuring a multi-level task organization system, users can create tasks, subtasks, and subsubtasks to capture the details of their work or personal projects. With built-in user authentication, each user can maintain their private list, accessible only after logging in.

# Project structure
```
todo-app/
├── app/
│   ├── __init__.py
│   ├── models.py            # Database models
│   ├── auth.py              # Authentication routes
│   └── main.py              # Todo list routes
│
├── static/
│   ├── styles.css
│   └── scripts.js
│   
└── templates/               
    ├── base.html
    ├── index.html
    ├── auth_pages           # All html pages related to Authentication
    │   ├──login.html
    │   └──signup.html
    │ 
    └── todo_pages           # All html pages related to Todo lists
        ├──todo.html
        ├──list.html
        ├──task.html
        ├──subtask.html
        └──subsubtask.html
```

# Features

- User Authentication: Secure signup and login functionality to keep your tasks private and personalized. Corresponding pages and routes can found in **auth_pages** folder and **auth.py** respectively. All of data is stored in SQLAlchemy generated database in **models.py**.

- Hierarchical Todo Lists: Create multiple lists for different purposes with tasks, subtasks, and subsubtasks to organize them with granularity. Add, edit, and delete both lists and tasks.Corresponding pages and routes can be found in **todo_pages** and **main.py** respectively.

- Interactive UI: Drag and drop tasks to reorganize them. Expand or collapse task views for a streamlined experience. For details go to **scripts.js**.

# Installation
In order to run the app, use the following commands:
```
python3 -m venv venv
source venv/bin/activate
cd path/cs162_assignment-main
pip3 install -r requirements.txt
export FLASK_APP=project
flask run
```
# Demo

https://www.loom.com/share/690155c400fd4cd399e99558439276c9?sid=98e4a3df-8f02-4606-a24d-a058e21736ae

# Possible improvements
- Fixing "Rename" and "Add Task" buttons to get rid off double clicks. 
- Reduce redundancy in **todo_pages** by using **tasks.html** recursivelly. 
