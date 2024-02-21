from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_session import Session, SqlAlchemySessionInterface
from flask_migrate import Migrate
from app.config import App_Config
from flask_restx import Api
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
sess = Session()
migrate = Migrate()
bcrypt = Bcrypt()
api = Api(
    version="1.0",
    title="Contact API",
    description="API for managing contacts 092a34a279d9446c97f1525b7803ded9",
    url_prefix="/api/v1",
)


def create_app():
    """
    Create a Flask app.
    """
    # Initialize Flask
    app = Flask(__name__)
    app.config["SESSION_SQLALCHEMY"] = db

    # Load configuration from App_Config
    app.config.from_object(App_Config)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Initialize CORS
    CORS(app, supports_credentials=True)

    # Initialize Flask extensions
    db.init_app(app)
    sess.init_app(app)
    SqlAlchemySessionInterface(app, db, "session", "_sess")
    migrate.init_app(app, db)
    api.init_app(app)
    bcrypt.init_app(app)

    # Import namespace
    from app.auth.routes import auth_ns
    from app.user.routes import user_ns
    from app.aid.routes import help_ns

    # Register namespace
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(help_ns)

    with app.app_context():
        # Create database tables
        db.create_all()
        print("Database created successfully")

    return app
