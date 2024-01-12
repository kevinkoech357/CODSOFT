from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from app.config import App_Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()
csrf = CSRFProtect()


def create_app():
    """
    Create a Flask app.
    """
    # Initialize Flask
    app = Flask(__name__)

    # Load configuration from App_Config
    app.config.from_object(App_Config)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Initialize CORS
    CORS(app)

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    # Import blueprints
    from app.auth.routes import auth
    #from app.user.routes import user

    # Register blueprints
    app.register_blueprint(auth)
    #app.register_blueprint(user)

    # Import models
    from app.models.user import User

    with app.app_context():
        # Create database tables
        db.create_all()
        print("Database created successfully")

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    login_manager.login_message = "Login to continue."
    login_manager.login_message_category = "info"

    return app
