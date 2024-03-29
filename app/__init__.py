"""
Initialisation file for the project
here I define all main variable such a
db - database, migrate - migration manager and ect.
"""
from flask import Flask
from config import config
from .main.views import main_bp
from .user.views import user_bp
from .articles.views import articles_bp
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor

db = SQLAlchemy()
login_manager = LoginManager()
ckeditor = CKEditor()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(articles_bp)

    app.secret_key = "super_secret_key_ever!"

    return app


app = create_app()

@login_manager.user_loader
def load_user(user_id):
    """ This function sets up model that used as User model"""
    from app.models import User
    return User.query.get(int(user_id))
