"""
Entry point of the Flask web application.

Bootstraps the app, initializes UI components, and provides a route
to download the SQLite database.
"""

from flask import Flask, send_file
from flask_bootstrap import Bootstrap
from . import create_app
from .config import Config
import os

# Create the Flask app with configuration
app = create_app(Config)

# Initialize Flask-Bootstrap for UI styling
bootstrap = Bootstrap(app)

@app.route('/download-db')
def download_db():
    """
    Route to download the SQLite database file.

    Returns:
        Response: Sends the database file as an attachment.
    """
    db_path = os.path.join(app.root_path, '..', 'instance', 'proj.db')
    return send_file(db_path, as_attachment=True)

if __name__ == '__main__':
    # Ensure database tables are created before starting the app
    with app.app_context():
        app.db.create_all()

    # Run the Flask development server
    app.run()