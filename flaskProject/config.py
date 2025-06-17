import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super secret key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///proj.db"
    SQL_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False