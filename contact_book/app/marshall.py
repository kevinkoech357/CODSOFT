from flask_restx import fields
from app import api


# Define DTOs (Data Transfer Objects) for request and response payloads
registration_model = api.model(
    "UserRegistration",
    {
        "username": fields.String(required=True, description="Username"),
        "email": fields.String(required=True, description="Email address"),
        "password": fields.String(required=True, description="Password"),
    },
)

login_model = api.model(
    "UserLogin",
    {
        "username": fields.String(
            required=True, description="Username or Email address"
        ),
        "password": fields.String(required=True, description="Password"),
    },
)


contact_model = api.model(
    "Contact",
    {
        "id": fields.String,
        "user_id": fields.String,
        "contact_name": fields.String,
        "phone_number": fields.String,
        "email": fields.String,
        "address": fields.String,
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
    },
)

user_model = api.model(
    "User",
    {
        "id": fields.String,
        "email": fields.String,
        "created_at": fields.DateTime,
    },
)

create_contact_model = api.model(
    "CreateContact",
    {
        "contact_name": fields.String,
        "phone_number": fields.String,
        "email": fields.String,
        "address": fields.String,
    },
)
