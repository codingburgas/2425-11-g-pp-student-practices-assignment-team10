"""
Initializes the Flask application, database, and login manager.

Defines the application factory function `create_app` for creating instances
of the app with different configurations.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
# Initialize SQLAlchemy and LoginManager without an app context
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config):
    """
    Application factory function.

    Initializes the Flask app, loads config, registers extensions and blueprints.

    Args:
        config (object): A config class containing Flask configuration variables.

    Returns:
        Flask: The fully configured Flask application instance.
    """
    app = Flask(__name__)
    if config == 'testing':
        app.config.from_mapping({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'WTF_CSRF_ENABLED': False,
            'SECRET_KEY': 'test',
        })
    else:
        app.config.from_object(config)

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    from .auth import auth_bp
    from .main import main_bp
    from .form import form_bp
    from .ml import ml_bp
    from .auth.models import User

    @login_manager.user_loader
    def load_user(user_id):
        """
        Flask-Login user loader callback.

        Args:
            user_id (int): ID of the user to load.

        Returns:
            User: User instance if found, else None.
        """
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(form_bp)
    app.register_blueprint(ml_bp)

    return app