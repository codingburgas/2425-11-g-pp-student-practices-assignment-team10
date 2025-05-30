from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import form_bp
from .forms import StudentSurveyForm, TeacherSurveyForm
from .models import StudentSurveyResponse
from flaskProject import db

@form_bp.route('/survey/student', methods=['GET', 'POST'])
@login_required
def student_survey():
    if current_user.role != 'student':
        flash("Only students can access this survey.", "warning")
        return redirect(url_for('main.dashboard'))
    form = StudentSurveyForm()
    if form.validate_on_submit():
        # Проверка дали вече е попълнил анкетата
        existing_response = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
        if existing_response:
            flash("You have already submitted this survey.", "info")
            return redirect(url_for('main.profile'))
        # Създаване на нов запис
        response = StudentSurveyResponse(
            student_id=current_user.id,
            favorite_subject=form.favorite_subject.data,
            learning_style=form.learning_style.data,
            strength=form.strength.data,
            future_study=form.future_study.data,
            class_behavior=form.class_behavior.data,
            activities=form.activities.data,
            goal=form.goal.data
        )
        db.session.add(response)
        db.session.commit()
        flash("Survey submitted successfully!", "success")
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