from flask_restx import Resource, Namespace
from app.models.user import User
from app.marshall import user_model

help_ns = Namespace("help", description="Get user_id to perform CRUD Op.")


@help_ns.route("/users")
class UsersResource(Resource):
    @help_ns.doc("get user id")
    @help_ns.marshal_list_with(user_model)
    def get(self):
        """
        Get all users
        """
        return User.query.all()
