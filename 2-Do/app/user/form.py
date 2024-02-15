from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, TimeField
from wtforms.validators import DataRequired


class CreateTodoForm(FlaskForm):
    title = StringField(
        "Todo Title", validators=[DataRequired(message="Title is required.")]
    )
    content = TextAreaField(
        "Todo Content", validators=[DataRequired(message="Content is required.")]
    )
    category_choices = [
        ("School", "School"),
        ("Chores", "Chores"),
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Health", "Health"),
        ("Social", "Social"),
        ("Recreation", "Recreation"),
    ]
    category = SelectField(
        "Todo Category",
        choices=category_choices,
        validators=[DataRequired(message="Category is required.")],
    )
    start_time = TimeField(
        "Start Time", validators=[DataRequired(message="Start time is required.")]
    )
    end_time = TimeField(
        "End Time", validators=[DataRequired(message="End time is required.")]
    )
    submit = SubmitField("Create Todo")


class EditTodoForm(FlaskForm):
    title = StringField(
        "Todo Title", validators=[DataRequired(message="Title is required.")]
    )
    content = TextAreaField(
        "Todo Content", validators=[DataRequired(message="Content is required.")]
    )
    category_choices = [
        ("School", "School"),
        ("Chores", "Chores"),
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Health", "Health"),
        ("Social", "Social"),
        ("Recreation", "Recreation"),
    ]
    category = SelectField(
        "Todo Category",
        choices=category_choices,
        validators=[DataRequired(message="Category is required.")],
    )
    submit = SubmitField("Update Todo")
