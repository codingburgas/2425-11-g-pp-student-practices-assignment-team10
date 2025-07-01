"""Defines the routes for the main blueprint, including profile, admin, and community features."""

from flaskProject.form.models import StudentSurveyResponse, TeacherSurveyResponse
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_required, current_user
from flaskProject.auth.models import User
from .. import db
from . import main_bp
from flaskProject.auth.forms import EditProfileForm
from .models import Comment
from ..utils.error_handler import render_error_page
from flaskProject.ml.model import LogisticRegression
from flaskProject.ml.utils import encode_features
import numpy as np
from flaskProject.utils.metrics import compute_metrics

@main_bp.route('/')
def index():
    """
    Render the home page and train the AI model using all student-teacher pairs.
    """
    try:
        students = StudentSurveyResponse.query.all()
        teachers = {t.teacher_id: t for t in TeacherSurveyResponse.query.all()}
        dataset = []

        for student in students:
            for teacher_id, teacher in teachers.items():
                features = encode_features(student, teacher)
                label = 1 if student.mentor_id == teacher_id else 0
                dataset.append(features + [label])

        if dataset:

            n_features = len(dataset[0]) - 1
            model = LogisticRegression(n_features=n_features)
            model.train(dataset, epochs=10000, learning_rate=0.0001)

            X = np.array([d[:-1] for d in dataset])
            y_true = np.array([d[-1] for d in dataset])
            y_pred = np.array([model.predict_class(x) for x in X])
            y_proba = np.array([model.predict_proba(x) for x in X])

            # Save model state
            session["model_weights"] = model.weights.tolist()
            session["model_bias"] = model.bias


            session["model_metrics"] = compute_metrics(y_true, y_pred, y_proba)
        else:
            session["model_metrics"] = None
            session["model_weights"] = None
            session["model_bias"] = None
        print(session["model_metrics"])
        return render_template(
            'index.html',
            model_accuracy=session["model_metrics"]["accuracy"] if session["model_metrics"] else "N/A"
        )
    except Exception as e:
        return render_error_page(e)


@main_bp.route('/metrics')
@login_required
def model_metrics():
    """
    Display evaluation metrics for the latest trained model.
    """
    try:
        metrics = session["model_metrics"]
        if not metrics:
            flash("Model has not been trained yet or there is no data.", "warning")
            return redirect(url_for("main.index"))
        return render_template("metrics.html", metrics=metrics)
    except Exception as e:
        return render_error_page(e)


@main_bp.route('/profile')
@login_required
def profile():
    """
    Display the user's profile page.

    Shows survey status and assigned mentees if the user is a teacher.
    """
    try:
        if session.get("prediction"):
            session["prediction"] = None

        has_survey = False
        mentees = []

        if current_user.role == 'student':
            has_survey = StudentSurveyResponse.query.filter_by(student_id=current_user.id).first() is not None
        elif current_user.role == 'teacher':
            has_survey = TeacherSurveyResponse.query.filter_by(teacher_id=current_user.id).first() is not None
            mentees = StudentSurveyResponse.query.filter_by(mentor_id=current_user.id).all()

        return render_template('profile.html', user=current_user, has_survey=has_survey, mentees=mentees)
    except Exception as e:
        return render_error_page(e)


@main_bp.route('/admin/users')
@login_required
def admin_users():
    """
    Display a list of all users to admin users only.
    """
    try:
        if not current_user.is_admin:
            flash("Unauthorized")
            return redirect(url_for('main.index'))

        users = User.query.all()
        return render_template('admin/users.html', users=users)
    except Exception as e:
        return render_error_page(e)


@main_bp.route('/admin/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    """
    Delete a user account (admin-only). Prevents deletion of the main admin.
    """
    try:
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
    except Exception as e:
        return render_error_page(e)


@main_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    Allow a logged-in user to edit their profile information.
    Validates uniqueness of username and email.
    """
    try:
        form = EditProfileForm(obj=current_user)

        if form.validate_on_submit():
            if form.username.data != current_user.username and User.query.filter_by(username=form.username.data).first():
                flash('Username already taken.')
                return redirect(url_for('main.edit_profile'))

            if form.email.data != current_user.email and User.query.filter_by(email=form.email.data).first():
                flash('Email already in use.')
                return redirect(url_for('main.edit_profile'))

            current_user.username = form.username.data
            current_user.email = form.email.data
            if form.password.data:
                current_user.set_password(form.password.data)

            db.session.commit()
            flash('Profile updated successfully!')
            return redirect(url_for('main.profile'))

        return render_template('edit_profile.html', form=form)
    except Exception as e:
        return render_error_page(e)

@main_bp.route('/community')
@login_required
def community():
    """
    Display all users and their survey responses in a community view.
    """
    try:
        users = User.query.all()
        student_responses = {resp.student_id: resp for resp in StudentSurveyResponse.query.all()}
        teacher_responses = {resp.teacher_id: resp for resp in TeacherSurveyResponse.query.all()}

        return render_template('community.html', users=users,
                               student_responses=student_responses,
                               teacher_responses=teacher_responses)
    except Exception as e:
        return render_error_page(e)

@main_bp.route('/view_profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def view_profile(user_id):
    """
    View another user's profile and post a comment.

    Handles both GET (view profile) and POST (submit comment) methods.
    """
    try:
        user = User.query.get_or_404(user_id)
        comments = Comment.query.filter_by(user_id=user_id).order_by(Comment.timestamp.desc()).all()

        if request.method == 'POST':
            content = request.form.get('content')
            if content:
                new_comment = Comment(content=content, user_id=current_user.id)
                db.session.add(new_comment)
                db.session.commit()
                flash('Comment posted successfully!', 'success')
                return redirect(url_for('main.view_profile', user_id=user_id))
            else:
                flash('Comment cannot be empty.', 'danger')

        return render_template('profile.html', user=user, comments=comments)
    except Exception as e:
        return render_error_page(e)