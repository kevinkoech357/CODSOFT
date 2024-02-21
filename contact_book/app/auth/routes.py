from flask import request, session
from flask_restx import Resource, Namespace, abort
from app.models.user import User
from app import db
from app.marshall import registration_model, login_model
from email_validator import validate_email, EmailNotValidError

# Create a namespace for authentication routes
auth_ns = Namespace("auth", description="Authentication operations", validate=True)


@auth_ns.route("/register")
@auth_ns.doc(params={"username": "Username", "email": "Email", "password": "Password"})
class UserRegistration(Resource):
    @auth_ns.expect(registration_model)
    def post(self):
        """User registration endpoint."""
        data = auth_ns.payload
        username = data["username"]
        email = data["email"]
        password = data["password"]

        # Validate email
        try:
            v = validate_email(email)
            email = v["email"]
        except EmailNotValidError:
            return {"status": "error", "message": "Invalid email address"}, 400

        # Check if username is already registered
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            abort(400, "Username already taken", status="error")

        # Check if email is already registered
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            abort(400, "Email address already taken.")

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Json user details
        user_details = {
            "user_id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        }

        session["user"] = {"id": new_user.id}

        return user_details, 200


@auth_ns.route("/login")
class UserLogin(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """User login endpoint."""
        data = request.json
        username_or_email = data["username"]
        password = data["password"]

        # Find the user by username or email
        user = User.query.filter(
            (User.username == str(username_or_email))
            | (User.email == str(username_or_email))
        ).first()

        if user and user.check_password(password):
            # Set the user session
            user = session.get("user")

            return {"status": "success", "message": "Login successful"}, 200

        return {"status": "error", "message": "Invalid username or password"}, 401


@auth_ns.route("/logout")
class UserLogout(Resource):
    def post(self):
        """User logout endpoint."""
        # Clear the user session
        session.pop("user_id", None)
        return {"status": "success", "message": "Logout successful"}, 200
