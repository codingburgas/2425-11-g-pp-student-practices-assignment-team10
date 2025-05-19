from flaskProject import create_app, db
from flaskProject.config import Config
from flaskProject.auth.models import User

app = create_app(Config)

with app.app_context():
    # Drop all existing tables
    """db.drop_all()
    print("Dropped all tables")"""

    # Create all tables
    db.create_all()