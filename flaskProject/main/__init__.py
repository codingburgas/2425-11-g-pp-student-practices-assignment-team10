"""Initialize the main Blueprint for the application."""

from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import routes