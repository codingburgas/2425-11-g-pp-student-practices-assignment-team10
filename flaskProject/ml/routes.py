"""
Routes for the ML Blueprint, providing mentor matching functionality
based on a logistic regression model.
"""

from flask import render_template, Blueprint, redirect, url_for, session
from flask_login import login_required, current_user
from .model import LogisticRegression
from .utils import encode_features
from ..form.models import StudentSurveyResponse, TeacherSurveyResponse
from . import ml_bp
from flaskProject import db
from ..utils.error_handler import render_error_page


@ml_bp.route('/match')
@login_required
def match():
    """
    Perform mentor-student matching using a logistic regression model.

    Returns:
        Renders a template with sorted matches based on predicted probabilities.
    """
    try:
        if current_user.role != 'student':
            return redirect(url_for('main.index'))
        student_data = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
        teachers = TeacherSurveyResponse.query.all()
        if not student_data or not teachers:
            return render_template('no_data.html')
        matches = []
        if not session.get('prediction'):
            for teacher in teachers:
                features = encode_features(student_data, teacher)
                model = LogisticRegression(n_features=len(features))
                score = model.predict_proba(features)
                matches.append((
                    teacher.teacher.username,
                    round(score, 2),
                    teacher.teacher.id,
                    student_data.mentor_id == teacher.teacher.id
                ))
            matches.sort(key=lambda x: x[1], reverse=True)
            session['prediction'] = matches
        return render_template('matches.html', matches=session['prediction'])
    except Exception as e:
        return render_error_page(e)

@ml_bp.route('/match/signup/<int:teacher_id>', methods=['POST'])
@login_required
def signup_mentor(teacher_id):
    """
    Assign a teacher as the student's mentor.

    Args:
        teacher_id (int): ID of the selected mentor.

    Returns:
        Redirects to the match results page.
    """
    try:
        if current_user.role != 'student':
            return redirect(url_for('main.index'))
        student = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
        if not student:
            return redirect(url_for('main.profile'))
        student.mentor_id = teacher_id
        db.session.commit()
        return redirect(url_for('ml.match'))
    except Exception as e:
        return render_error_page(e)