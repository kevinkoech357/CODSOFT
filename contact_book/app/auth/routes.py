from flask import request, session
from flask_restx import Resource, Namespace
from app.models.user import User
from app import db
from app.marshall import registration_model, login_model

# Create a namespace for authentication routes
auth_ns = Namespace("auth", description="Authentication operations")


@auth_ns.route("/register")
class UserRegistration(Resource):
    @auth_ns.expect(registration_model)
    def post(self):
        """User registration endpoint."""
        data = auth_ns.payload
        username = data["username"]
        email = data["email"]
        password = data["password"]

        # Validate email
        # try:
        #    v = validate_email(email)
        #   email = v["email"]
        # except EmailNotValidError:
        #   return {"status": "error", "message": "Invalid email address"}, 400

        # Check if username is already registered
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            return {"status": "error", "message": "Username already taken!"}, 400

        # Check if email is already registered
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return {"status": "error", "message": "Invalid email address"}, 400

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Placeholder for to_dict function, replace with your actual implementation
        user_details = {
            "user_id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        }

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
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

        if user and user.check_password(password):
            # Set the user session
            session["user_id"] = user.id
            return {"success": "Login successful"}, 200

        return {"error": "Invalid username or password"}, 401


@auth_ns.route("/logout")
class UserLogout(Resource):
    def post(self):
        """User logout endpoint."""
        # Clear the user session
        session.clear()
        return {"success": "Logout successful"}, 200
