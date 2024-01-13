import uuid
import moment
import datetime
from app import db
from sqlalchemy import func


def generate_uuid():
    return str(uuid.uuid4().hex)


class Contact(db.Model):
    """
    Model representing a contact in the contact book.

    Attributes:
        id (str): The unique identifier for the contact.
        user_id (str): The foreign key referencing the user to whom the contact belongs.
        contact_name (str): The first name of the contact.
        phone_number (str): The phone number of the contact.
        email (str): The email address of the contact.
        address (str): The address of the contact.
        created_at (str): Human-readable timestamp indicating when the contact was created.
        updated_at (str): Human-readable timestamp indicating when the contact was last updated.
    """

    __tablename__ = "contacts"

    id = db.Column(db.String(32), default=generate_uuid, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False)
    contact_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    created_at = db.Column(
        db.String, default=moment.utcnow().format("YYYY-MM-DD HH:mm:ss"), nullable=False
    )
    updated_at = db.Column(
        db.String,
        onupdate=moment.utcnow().format("YYYY-MM-DD HH:mm:ss"),
        nullable=False,
    )

    def __repr__(self):
        return f"Contact(id={self.id}, user_id={self.user_id}, name='{self.name}', phone_number='{self.phone_number}', email='{self.email}', address='{self.address}', created_at={self.created_at}, updated_at={self.updated_at})"
