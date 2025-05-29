from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import form_bp
from .forms import StudentSurveyForm, TeacherSurveyForm



@form_bp.route('/survey/student', methods=['GET', 'POST'])
@login_required
def student_survey():
    if current_user.role != 'student':
        flash("Only students can access this survey.", "warning")
        return redirect(url_for('main.dashboard'))

    form = StudentSurveyForm()
    if form.validate_on_submit():
        # Тук по-късно ще се записват отговорите
        return render_template('thank_you.html')
    return render_template('surveys/student_survey.html', form=form)



@form_bp.route('/survey/teacher', methods=['GET', 'POST'])
@login_required
def teacher_survey():
    if current_user.role != 'teacher':
        flash("Only teachers can access this survey.", "warning")
        return redirect(url_for('main.dashboard'))

    form = TeacherSurveyForm()
    if form.validate_on_submit():
        # Тук по-късно ще се записват отговорите
        return render_template('thank_you.html')
    return render_template('surveys/teacher_survey.html', form=form)
