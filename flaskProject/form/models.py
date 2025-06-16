"""Define database models for storing student and teacher survey responses."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from ..auth.models import User
from flaskProject import db


class StudentSurveyResponse(db.Model):
    """
    Model representing a student's responses to the survey.

    Attributes:
        - student_id: Foreign key to User, unique
        - mentor_id: (optional) Foreign key to assigned mentor
        - Survey response fields: favorite_subject, learning_style, etc.
    """
    __tablename__ = 'student_survey_responses'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Optional mentor reference

    favorite_subject = db.Column(db.String(50), nullable=False)
    learning_style = db.Column(db.String(50), nullable=False)
    strength = db.Column(db.String(50), nullable=False)
    future_study = db.Column(db.String(50), nullable=False)
    class_behavior = db.Column(db.String(50), nullable=False)
    activities = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(50), nullable=False)

    student = db.relationship('User', foreign_keys=[student_id], backref=db.backref('survey_response', uselist=False))
    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='mentees')

    def __repr__(self):
        return f'<SurveyResponse student_id={self.student_id}>'


class TeacherSurveyResponse(db.Model):
    """
    Model representing a teacher's mentoring preferences and strengths.

    Attributes:
        - teacher_id: Foreign key to User, unique
        - Survey response fields: favorite_subjects_to_mentor, teaching_style, etc.
    """
    __tablename__ = 'teacher_survey_responses'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    favorite_subjects_to_mentor = db.Column(db.String(50), nullable=False)
    teaching_style = db.Column(db.String(50), nullable=False)
    strengths = db.Column(db.String(50), nullable=False)
    student_type_preference = db.Column(db.String(50), nullable=False)
    extracurricular_focus = db.Column(db.String(50), nullable=False)
    mentorship_goal = db.Column(db.String(50), nullable=False)

    teacher = db.relationship('User', backref=db.backref('teacher_survey_response', uselist=False))

    def __repr__(self):
        return f'<TeacherSurveyResponse teacher_id={self.teacher_id}>'