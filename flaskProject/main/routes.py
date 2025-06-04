from flask import render_template
from flask_login import login_required, current_user
from . import main_bp
from flaskProject.form.models import StudentSurveyResponse, TeacherSurveyResponse


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/profile')
@login_required
def profile():
    has_survey = False
    if current_user.role == 'student':
        has_survey = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first() is not None
    elif current_user.role == 'teacher':
        has_survey = TeacherSurveyResponse.query.filter_by(teacher_id=current_user.id).first() is not None

    return render_template('profile.html', user=current_user, has_survey=has_survey)