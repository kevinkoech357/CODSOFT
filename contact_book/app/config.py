import os
import datetime
from dotenv import load_dotenv

load_dotenv(".env")


class App_Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "contact_book_api")
    # Database URI. Default is SQLite in-memory database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
    )
    # Disable modification tracking for SQLAlchemy, unless explicitly set to True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Disable echoing SQL statements to the console
    SQLALCHEMY_ECHO = False

    # Session App_Config
    SESSION_TYPE = "sqlalchemy"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)

    # RestX App_Config
    RESTX_VALIDATE = True
