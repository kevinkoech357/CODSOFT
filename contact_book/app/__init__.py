from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from flask_session import Session
from flask_migrate import Migrate
from app.config import App_Config
from flask_restx import Api, Namespace
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
# sess = Session()
migrate = Migrate()
bcrypt = Bcrypt()
api = Api(
    version="1.0",
    title="Contact Book API",
    description="A simple Contact Book API",
)


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
    # sess.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    bcrypt.init_app(app)

    # Import namespace
    from app.auth.routes import auth_ns
    from app.user.routes import user_ns

    # Register namespace
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)

    with app.app_context():
        # Create database tables
        db.create_all()
        print("Database created successfully")

    return app
