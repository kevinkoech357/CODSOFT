from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    identifier = StringField(
        "Username or Email",
        validators=[
            DataRequired(message="Username or email is required."),
            Length(
                min=3, max=30, message="Username must be between  3 and  30 characters."
            ),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Password is required.")]
    )
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(
                min=3, max=20, message="Username must be between  3 and  20 characters."
            ),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email address."),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Password is required.")]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Confirm password is required."),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    submit = SubmitField("Register")


class ResetPasswordForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email address."),
        ],
    )
    new_password = PasswordField(
        "New Password", validators=[DataRequired(message="New password is required.")]
    )
    confirm_new_password = PasswordField(
        "Confirm New Password",
        validators=[
            DataRequired(message="Confirm new password is required."),
            EqualTo("new_password", message="New passwords must match."),
        ],
    )
    submit = SubmitField("Reset Password")
