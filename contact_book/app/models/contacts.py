import uuid
from datetime import datetime
from app import db
from sqlalchemy import func


def generate_uuid():
    return str(uuid.uuid4())


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

    id = db.Column(db.String(36), default=generate_uuid, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    contact_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime,
        onupdate=func.now(),
        nullable=False,
        server_default=func.now(),
    )

    def __repr__(self):
        return f"Contact(id={self.id}, user_id={self.user_id}, contact_name='{self.contact_name}', phone_number='{self.phone_number}', email='{self.email}', address='{self.address}', created_at={self.created_at.isoformat()}, updated_at={self.updated_at.isoformat()})"
