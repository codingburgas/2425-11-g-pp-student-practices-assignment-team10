

from flask import Flask
from flask_bootstrap import Bootstrap

from . import create_app
from .config import Config

app = create_app(Config)
bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run()
