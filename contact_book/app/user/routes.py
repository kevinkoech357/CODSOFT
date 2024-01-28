from flask import request
from flask_restx import Resource, Namespace
from app.models.user import User
from app.models.contacts import Contact
from app import db
from app.utils import is_valid_uuid
from app.marshall import (
    contact_model,
    create_contact_model,
)


user_ns = Namespace("contact", description="CRUD Operations for Contacts")


@user_ns.route("/contacts/<string:user_id>")
class UserContacts(Resource):
    @user_ns.marshal_list_with(contact_model)
    def get(self, user_id):
        """Retrieve all contacts for a specific user."""
        # Check if user_id is a valid UUID
        if not is_valid_uuid(user_id):
            return {"error": "Invalid UUID format"}

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found"}

        # Retrieve user_contacts using the relationship between User and Contacts models
        user_contacts = Contact.query.filter_by(user_id=user.id).all()

        if not user_contacts:
            return {"error": "No contacts added yet!"}

        # Return the list of contact dictionaries
        return user_contacts, 200


@user_ns.route("/create-contact/<string:user_id>")
class NewUserContact(Resource):
    @user_ns.expect(create_contact_model)
    @user_ns.marshal_with(contact_model, code=201)
    def post(self, user_id):
        """Add a new contact."""
        if not is_valid_uuid(user_id):
            return {"error": "Invalid UUID format"}, 400

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found"}, 404

        data = user_ns.payload
        contact_name = data["contact_name"]
        phone_number = data["phone_number"]
        email = data["email"]
        address = data["address"]

        new_contact = Contact(
            user_id=user.id,
            contact_name=contact_name,
            phone_number=phone_number,
            email=email,
            address=address,
        )

        db.session.add(new_contact)
        db.session.commit()

        return new_contact, 200


@user_ns.route("/update-contact/<string:user_id>/<string:contact_id>")
class UserContact(Resource):
    @user_ns.expect(create_contact_model)
    @user_ns.marshal_with(contact_model)
    def put(self, user_id, contact_id):
        """Modify an existing contact."""
        if not is_valid_uuid(user_id):
            return {"error": "Invalid UUID format"}, 400

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found"}, 404

        if not is_valid_uuid(contact_id):
            return {"error": "Invalid Contact ID format"}, 400

        existing_contact = Contact.query.filter_by(
            id=contact_id, user_id=user.id
        ).first()

        if not existing_contact:
            return {"error": "Contact not found"}, 404

        data = request.json

        # Update contact details
        existing_contact.contact_name = data.get("contact_name")
        existing_contact.phone_number = data.get("phone_number")
        existing_contact.email = data.get("email")
        existing_contact.address = data.get("address")

        db.session.commit()

        return existing_contact, 200


@user_ns.route("/delete-contact/<string:user_id>/<string:contact_id>")
class DeleteContact(Resource):
    def delete(self, user_id, contact_id):
        """Delete an existing contact."""
        if not is_valid_uuid(user_id):
            return {"error": "Invalid UUID format"}, 400

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found"}, 404

        if not is_valid_uuid(contact_id):
            return {"error": "Invalid Contact ID format"}, 400

        existing_contact = Contact.query.filter_by(
            id=contact_id, user_id=user.id
        ).first()

        if not existing_contact:
            return {"error": "Contact not found"}, 404

        # Delete the contact
        db.session.delete(existing_contact)
        db.session.commit()

        return {"success": "Contact deleted successfully"}, 200


@user_ns.route("/<string:user_id>/<string:contact_id>")
class OneContact(Resource):
    @user_ns.marshal_with(contact_model)
    def get(self, user_id, contact_id):
        """Get details of a specific contact"""
        if not is_valid_uuid(user_id):
            return {"error": "Invalid UUID format"}, 400

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found"}, 404

        if not is_valid_uuid(contact_id):
            return {"error": "Invalid Contact ID format"}, 400

        existing_contact = Contact.query.filter_by(
            id=contact_id, user_id=user.id
        ).first()

        if not existing_contact:
            return {"error": "Contact not found"}, 404

        return existing_contact, 200
