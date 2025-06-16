"""
This module defines the User model used for authentication and user management.
"""

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import db


class User(UserMixin, db.Model):
    """
    User model that includes authentication and role-based access.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin privilege flag

    def set_password(self, password):
        """
        Hash and set the user's password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check the user's password against the stored hash.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        Return a string representation of the User instance.
        """
        return f'<User {self.username}>'