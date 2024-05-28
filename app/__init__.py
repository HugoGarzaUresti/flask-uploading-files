from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['UPLOAD_FOLDER'] = 'upload-dir'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit\
    app.secret_key= os.urandom(24)

    with app.app_context():
        from . import routes
        return app
