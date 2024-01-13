from datetime import datetime
from app import db
from sqlalchemy.orm import relationship
import uuid


# Helper function to generate a random UUID in hex format
def generate_uuid():
    return str(uuid.uuid4().hex)


class Todo(db.Model):
    """
    Todo model for representing tasks.

    Attributes:
        id (str): Unique task identifier.
        user_id (str): Foreign key referencing the user who created the task.
        title (str): Title of the task.
        content (str): Task content or description.
        category (str): Category of the task.
        start_time (datetime): Start time of the task.
        end_time (datetime): End time of the task.
        created_at (datetime): Timestamp of when the task was created.
        updated_at (datetime): Timestamp of when the task was last updated.

    Relationships:
        user (User): Reference to the User model indicating the user associated with the task.
    """

    __tablename__ = "todo"

    id = db.Column(
        db.String(32), primary_key=True, default=generate_uuid, nullable=False
    )
    user_id = db.Column(db.String(32), db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    content = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50))
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    created_at = db.Column(
        db.TIMESTAMP(timezone=True),
        server_default=db.func.current_timestamp(),
        nullable=False,
    )
    updated_at = db.Column(
        db.TIMESTAMP(timezone=True),
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
        nullable=False,
    )

    # Define a relationship between the Todo and User models
    user = relationship("User", back_populates="todos")

    def __init__(
        self,
        user,
        title,
        content,
        category,
        start_time=None,
        end_time=None,
        created_at=None,
        updated_at=None,
    ):
        """
        Initialize a new Todo instance.

        Args:
            user (User): The user who created the task.
            title (str): Title of the task.
            content (str): Task content or description.
            category (str): Category of the task.
            start_time (datetime, optional): Start time of the task.
            end_time (datetime, optional): End time of the task.
            created_at (datetime, optional): Timestamp of when the task was created.
            updated_at (datetime, optional): Timestamp of when the task was last updated.
        """
        self.user = user
        self.title = title
        self.content = content
        self.category = category
        self.start_time = start_time
        self.end_time = end_time
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self):
        """
        Return an official object representation.

        Returns:
            str: Object representation.
        """
        return f"<Todo(id={self.id}, user_id={self.user_id}, title={self.title}, content={self.content}, category={self.category}, start_time={self.start_time}, end_time={self.end_time}, created_at={self.created_at}, updated_at={self.updated_at})>"

    def format(self):
        """
        Format the object's attributes as a dictionary.

        Returns:
            dict: Dictionary containing task attributes.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
