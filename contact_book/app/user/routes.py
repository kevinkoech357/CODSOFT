from flask_restx import Resource, Namespace, abort
from app.models.user import User
from app.models.contacts import Contact
from app import db
from app.utils import is_valid_uuid
from app.marshall import (
    contact_model,
    create_contact_model,
)
from typing import List, Union

user_ns = Namespace("contact", description="CRUD Operations for Contacts")


@user_ns.route("/<string:user_id>")
class UserContacts(Resource):
    @user_ns.marshal_list_with(contact_model)
    def get(self, user_id: str) -> Union[List[dict], dict]:
        """
        Retrieve all contacts for a specific user.

        Args:
            user_id (str): User id in uuid format

        Returns:
            A JSON response with user-contacts.
        """
        # Check if user_id is a valid UUID
        if not is_valid_uuid(user_id):
            abort(400, "Invalid user id format", status="error")

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, "User not found", status="error")

        # Retrieve user_contacts
        user_contacts = Contact.query.filter_by(user_id=user.id).all()

        if not user_contacts:
            abort(404, "User has not contacts", status="error")

        # Return the list of contact dictionaries
        return user_contacts, 200


@user_ns.route("/create/<string:user_id>")
class NewUserContact(Resource):
    @user_ns.expect(create_contact_model)
    @user_ns.marshal_with(contact_model, code=201)
    def post(self, user_id: str) -> Union[List[dict], dict]:
        """
        Add a new contact based on user ID.

        Args:
            user_id (str): User id in uuid format

        Returns:
            A JSON response with added contact details.
        """
        # Check if user_id is a valid UUID
        if not is_valid_uuid(user_id):
            abort(400, "Invalid user id format", status="error")

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, "User not found", status="error")

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


@user_ns.route("/update/<string:user_id>/<string:contact_id>")
class UserContact(Resource):
    @user_ns.expect(create_contact_model)
    @user_ns.marshal_with(contact_model, skip_none=True)
    def patch(self, user_id: str, contact_id: str) -> Union[List[dict], dict]:
        """
        Modify an existing contact.

        Args:
            user_id (str): User id in uuid format
            contact_id (str): Contact in in uuid formmat.

        Returns:
            A JSON response with modifiedcontact details.
        """
        # Check if user_id is a valid UUID
        if not is_valid_uuid(user_id) or not is_valid_uuid(contact_id):
            abort(400, "Invalid ID format", status="error")

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, "User not found", status="error")

        existing_contact = Contact.query.filter_by(id=contact_id).first()

        if not existing_contact:
            abort(404, "Contact not found", status="error")

        data = user_ns.payload

        # Get data payload
        data = user_ns.payload
        contact_name = data["contact_name"]
        phone_number = data["phone_number"]
        email = data["email"]
        address = data["address"]

        modified_contact = Contact(
            id=existing_contact.id,
            user_id=user.id,
            contact_name=contact_name,
            phone_number=phone_number,
            email=email,
            address=address,
        )

        db.session.commit()

        return modified_contact, 200


@user_ns.route("/delete/<string:user_id>/<string:contact_id>")
class DeleteContact(Resource):
    def delete(self, user_id: str, contact_id: str) -> Union[List[dict], dict]:
        """
        Delete an existing contact.

        Args:
            user_id(str): User id in uuid format
            contact_id(str): Contact id in uuid format

        Returns:
            JSON response.
        """
        if not is_valid_uuid(user_id) or not is_valid_uuid(contact_id):
            abort(400, "Invalid ID format", status="error")

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, "User not found", status="error")

        existing_contact = Contact.query.filter_by(id=contact_id).first()

        if not existing_contact:
            abort(404, "Contact not found", status="error")

        # Delete the contact
        db.session.delete(existing_contact)
        db.session.commit()

        return {"status": "success", "message": "Contact deleted successfully"}, 200


@user_ns.route("/<string:user_id>/<string:contact_id>")
class OneContact(Resource):
    @user_ns.marshal_with(contact_model)
    def get(self, user_id: str, contact_id: str) -> Union[List[dict], dict]:
        """
        Get details of a specific contact.

        Args:
            user_id(str): User id in uuid format
            contact_id(str): Contact id in uuid format

        Response:
            JSON response.
        """
        if not is_valid_uuid(user_id) or not is_valid_uuid(contact_id):
            abort(400, "Invalid ID format", status="error")

        # Retrieve the user based on user_id
        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, "User not found", status="error")

        existing_contact = Contact.query.filter_by(id=contact_id).first()

        if not existing_contact:
            abort(404, "Contact not found", status="error")

        return existing_contact, 200
