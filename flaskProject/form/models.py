from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

from ..auth.models import User

from flaskProject import db


class StudentSurveyResponse(db.Model):
    __tablename__ = 'student_survey_responses'

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    favorite_subject = db.Column(db.String(50), nullable=False)

    learning_style = db.Column(db.String(50), nullable=False)

    strength = db.Column(db.String(50), nullable=False)

    future_study = db.Column(db.String(50), nullable=False)

    class_behavior = db.Column(db.String(50), nullable=False)

    activities = db.Column(db.String(50), nullable=False)

    goal = db.Column(db.String(50), nullable=False)

    student = db.relationship('User', backref=db.backref('survey_response', uselist=False))

    def __repr__(self):
        return f'<SurveyResponse student_id={self.student_id}>'

