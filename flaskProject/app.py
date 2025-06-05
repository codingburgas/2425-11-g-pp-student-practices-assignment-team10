

from flask import Flask
from flask_bootstrap import Bootstrap

from . import create_app
from .config import Config
from flask import send_file
import os

app = create_app(Config)
bootstrap = Bootstrap(app)


@app.route('/download-db')
def download_db():
    db_path = os.path.join(app.root_path, '..','instance', 'proj.db')
    return send_file(db_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        app.db.create_all()
    app.run()
