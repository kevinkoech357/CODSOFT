from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, TimeField
from wtforms.validators import DataRequired


class CreateTodoForm(FlaskForm):
    title = StringField("Todo Title")
    content = TextAreaField("Todo Content", validators=[DataRequired()])
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
        "Todo Category", choices=category_choices, validators=[DataRequired()]
    )
    start_time = TimeField("Start Time", validators=[DataRequired()])
    end_time = TimeField("End Time", validators=[DataRequired()])
    submit = SubmitField("Create Todo")


class EditTodoForm(FlaskForm):
    title = StringField("Todo Title")
    content = TextAreaField("Todo Content", validators=[DataRequired()])
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
        "Todo Category", choices=category_choices, validators=[DataRequired()]
    )
    submit = SubmitField("Update Todo")
