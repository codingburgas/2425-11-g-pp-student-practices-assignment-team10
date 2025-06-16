from flask import Blueprint

# Create a Blueprint named 'auth' for authentication-related routes.
# The 'url_prefix' means all routes in this Blueprint will be prefixed with '/auth'.
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Import the routes module to register route handlers with this Blueprint.
# This ensures all route definitions in the 'routes' module are included under this Blueprint.
from . import routes