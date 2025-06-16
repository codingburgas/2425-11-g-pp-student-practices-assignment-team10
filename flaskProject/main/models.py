"""Defines the data models for comments used in the main blueprint."""

from datetime import datetime
from flaskProject import db
from ..auth.models import User

class Comment(db.Model):
    """Model representing a user comment on a profile or in the community section."""

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref='comments')

    def __repr__(self):
        """Return a string representation of the comment."""
        return f"<Comment by User {self.user_id}>"