from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import func
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model, UserMixin):
    """
    User model for representing user data.

    Attributes:
        id (str): Unique user identifier.
        username (str): User's last name.
        email (str): User's email address.
        password_hash (str): Hashed user password.
        created_at (datetime): Timestamp of when the user was created.

    Relationships:
        todo (List[Todo]): A list of todos associated with the user.
    """

    __tablename__ = "user"

    id = db.Column(
        db.String(32), primary_key=True, default=generate_uuid, nullable=False
    )
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
