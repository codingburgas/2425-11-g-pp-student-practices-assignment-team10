"""Initialize the form blueprint for handling student and teacher survey routes."""

from flask import Blueprint

# Blueprint configuration for all survey form routes
form_bp = Blueprint('form', __name__, url_prefix='/form')

# Import route handlers
from . import routes