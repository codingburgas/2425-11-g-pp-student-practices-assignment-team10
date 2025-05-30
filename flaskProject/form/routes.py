from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import form_bp
from .forms import StudentSurveyForm, TeacherSurveyForm
from .models import StudentSurveyResponse, TeacherSurveyResponse
from flaskProject import db


@form_bp.route('/survey/student', methods=['GET', 'POST'])
@login_required
def student_survey():
    if current_user.role != 'student':
        flash("Only students can access this survey.", "warning")
        return redirect(url_for('main.profile'))
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
        return redirect(url_for('main.profile'))

    form = TeacherSurveyForm()

    if form.validate_on_submit():
        existing_response = TeacherSurveyResponse.query.filter_by(teacher_id=current_user.id).first()
        if existing_response:
            flash("You have already submitted this survey.", "info")
            return redirect(url_for('main.profile'))

        response = TeacherSurveyResponse(
            teacher_id=current_user.id,
            favorite_subjects_to_mentor=form.favorite_subjects_to_mentor.data,
            teaching_style=form.teaching_style.data,
            strengths=form.strengths.data,
            student_type_preference=form.student_type_preference.data,
            extracurricular_focus=form.extracurricular_focus.data,
            mentorship_goal=form.mentorship_goal.data
        )

        db.session.add(response)
        db.session.commit()

        flash("Survey submitted successfully!", "success")
        return render_template('thank_you.html')

    return render_template('surveys/teacher_survey.html', form=form)