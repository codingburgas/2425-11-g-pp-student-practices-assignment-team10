from flask import render_template
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main_bp.route('/form')
@login_required
def form():
    return render_template('form_placeholder.html')  # Create this template