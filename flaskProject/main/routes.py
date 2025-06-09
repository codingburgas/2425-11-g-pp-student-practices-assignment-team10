from flaskProject.form.models import StudentSurveyResponse, TeacherSurveyResponse
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from flaskProject.auth.models import User
from .. import db
from . import main_bp


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


@main_bp.route('/admin/users')
@login_required
def admin_users():
    if not current_user.is_admin:
        flash("Unauthorized")
        return redirect(url_for('main.index'))

    users = User.query.all()
    return render_template('admin/users.html', users=users)


@main_bp.route('/admin/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash("Unauthorized")
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(user_id)
    if user.username == 'admin':
        flash("You can't delete the main admin!")
        return redirect(url_for('main.admin_users'))

    db.session.delete(user)
    db.session.commit()
    flash("User deleted.")
    return redirect(url_for('main.admin_users'))