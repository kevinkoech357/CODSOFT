from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app import App_Config

db = SQLAlchemy()

def create_app():
    """
    Create a flask app.
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


    return app
