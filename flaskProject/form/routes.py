"""Define route handlers for student and teacher survey submission and mentor matching."""

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import form_bp
from .forms import StudentSurveyForm, TeacherSurveyForm
from .models import StudentSurveyResponse, TeacherSurveyResponse
from flaskProject import db
from ..utils.error_handler import render_error_page


@form_bp.route('/survey/student', methods=['GET', 'POST'])
@login_required
def student_survey():
    """
    Handle student survey display and submission.

    - GET: Renders the survey form.
    - POST: Saves form responses to the database, if not previously submitted.
    """
    try:
        if current_user.role != 'student':
            flash("Only students can access this survey.", "warning")
            return redirect(url_for('main.profile'))

        form = StudentSurveyForm()
        if form.validate_on_submit():
            existing_response = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first()
            if existing_response:
                flash("You have already submitted this survey.", "info")
                return redirect(url_for('main.profile'))

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
            return redirect(url_for('form.find_mentor'))

        return render_template('surveys/student_survey.html', form=form)
    except Exception as e:
        return render_error_page(e)

@form_bp.route('/survey/teacher', methods=['GET', 'POST'])
@login_required
def teacher_survey():
    """
    Handle teacher survey display and submission.

    - GET: Renders the teacher survey form.
    - POST: Saves form responses to the database, if not previously submitted.
    """
    try:
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
    except Exception as e:
        return render_error_page(e)

@form_bp.route('/survey/find-mentor')
@login_required
def find_mentor():
    """
    Render the mentor matching results page for students.

    Access restricted to users with the 'student' role.
    """
    try:
        if current_user.role != 'student':
            flash("Only students can access this page.", "warning")
            return redirect(url_for('main.dashboard'))
        return render_template('surveys/find_mentor.html')
    except Exception as e:
        return render_error_page(e)