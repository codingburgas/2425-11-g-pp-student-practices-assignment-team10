"""
This module defines the authentication-related routes including login,
registration, and logout using Flask Blueprint.
"""

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

from . import auth_bp
from .forms import LoginForm, RegisterForm
from .models import User
from .. import db
from ..utils.error_handler import render_error_page


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.
    Redirects to profile page on success or displays error message on failure.
    If user is already logged in, redirects to profile.
    """
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('auth.login'))
            login_user(user)
            if user.is_admin:
                return redirect(url_for('main.admin_users'))
            else:
                return redirect(url_for('main.profile'))

        return render_template('auth/login.html', form=form)
    except Exception as e:
        return render_error_page(e)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle new user registration.
    Validates input, checks for existing users, and stores new user in database.
    Admin role is granted based on specific conditions.
    """
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))

        form = RegisterForm()
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                flash('Username already taken')
                return redirect(url_for('auth.register'))
            if User.query.filter_by(email=form.email.data).first():
                flash('Email already registered')
                return redirect(url_for('auth.register'))

            # Grant admin privileges based on strict conditions
            is_admin = (
                form.username.data == 'admin' and
                form.password.data == 'adminadmin' and
                form.role.data == 'teacher'
            )

            user = User(
                username=form.username.data,
                email=form.email.data,
                role=form.role.data,
                is_admin=is_admin
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('auth.login'))

        return render_template('auth/register.html', form=form)
    except Exception as e:
        return render_error_page(e)

@auth_bp.route('/logout')
@login_required
def logout():
    """
    Log the user out and redirect to homepage.
    """
    try:
        logout_user()
        return redirect(url_for('main.index'))
    except Exception as e:
        return render_error_page(e)