from flask import render_template, Blueprint, redirect, url_for, session
from flask_login import login_required, current_user
from .model import LogisticRegression
from .utils import encode_features
from ..form.models import StudentSurveyResponse, TeacherSurveyResponse
from . import ml_bp
from flaskProject import db
@ml_bp.route('/match')
@login_required
def match():
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
                teacher.teacher.id,  # teacher_id
                student_data.mentor_id == teacher.teacher.id  # is_signed_up
            ))
        matches.sort(key=lambda x: x[1], reverse=True)
        session['prediction'] = matches
    return render_template('matches.html', matches=session['prediction'])

@ml_bp.route('/match/signup/<int:teacher_id>', methods=['POST'])
@login_required
def signup_mentor(teacher_id):
    if current_user.role != 'student':
        return redirect(url_for('main.index'))
    student = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
    if not student:
        return redirect(url_for('main.profile'))
    student.mentor_id = teacher_id
    db.session.commit()
    return redirect(url_for('ml.match'))