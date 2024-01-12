from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    submit = SubmitField()


class RegistrationForm(FlaskForm):
    """
    Form for user registration.
    """

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


class ResetPasswordForm(FlaskForm):
    """
    Form for resetting user password.
    """

    email = StringField(
        "Email", validators=[validators.DataRequired(), validators.Email()]
    )
    new_password = PasswordField("New Password", validators=[validators.DataRequired()])
    confirm_new_password = PasswordField(
        "Confirm New Password",
        validators=[validators.DataRequired(), validators.EqualTo("new_password")],
    )
    submit = SubmitField("Reset Password")
