"""
This module defines Flask-WTF form classes for authentication-related features:
Login, Registration, and Profile Editing.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from .models import User


class LoginForm(FlaskForm):
    """
    Form for users to log in with username and password.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    """
    Form for users to register a new account with username, email, role, and password.
    Includes password confirmation and role selection.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired()])
    role = SelectField('Role', choices=[('student', 'Student'), ('teacher', 'Teacher')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password should be at least 8 characters long")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    submit = SubmitField('Register')


class EditProfileForm(FlaskForm):
    """
    Form to allow users to update their profile information.
    The password field is optional (used only if changing the password).
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('New Password (leave blank to keep current)')
    submit = SubmitField('Save Changes')