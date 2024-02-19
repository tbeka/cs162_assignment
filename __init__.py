from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        from . import auth
        from . import main
        db.create_all()

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    from .models import User
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app