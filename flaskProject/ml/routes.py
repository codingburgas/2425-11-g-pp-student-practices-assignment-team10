from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user
from .model import LogisticRegression
from .utils import encode_features
from ..form.models import StudentSurveyResponse, TeacherSurveyResponse
from flaskProject import db

ml_bp = Blueprint('ml', __name__, template_folder='templates')

@ml_bp.route('/match')
@login_required
def match():
    if current_user.role != 'student':
        return redirect(url_for('main.index'))

    student_data = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
    teachers = TeacherSurveyResponse.query.all()

    if not student_data or not teachers:
        return render_template('ml/no_data.html')

    matches = []
    for teacher in teachers:
        features = encode_features(student_data, teacher)
        model = LogisticRegression(n_features=len(features))
        # Без обучение – директно прогноза на база прилики
        score = model.predict_proba(features)
        matches.append((teacher.teacher.username, round(score, 2)))

    matches.sort(key=lambda x: x[1], reverse=True)

    return render_template('ml/matches.html', matches=matches)
