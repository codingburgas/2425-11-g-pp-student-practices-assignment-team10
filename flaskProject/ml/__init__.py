"""Initializes the ML Blueprint for machine learning-related routes."""

from flask import Blueprint

ml_bp = Blueprint('ml', __name__, url_prefix='/ml')

from . import routes