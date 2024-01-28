import uuid
from app import db, bcrypt
from sqlalchemy import func


def generate_uuid():
    return str(uuid.uuid4().hex)


class User(db.Model):
    """
    Model representing a user.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        contacts (list of Contact): List of contacts associated with the user.
        created_at (str): Human-readable timestamp indicating when the user was created.
    """

    __tablename__ = "users"

    id = db.Column(db.String(32), default=generate_uuid, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contacts = db.relationship("Contact", backref="user", lazy=True)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """
        Check if the provided password matches the user's hashed password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', created_at={self.created_at})"
