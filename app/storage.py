import os
from flask import current_app as app
from werkzeug.utils import secure_filename

def init_storage():
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def save_file(file, filename):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))

def get_files():
    return os.listdir(app.config['UPLOAD_FOLDER'])

def get_file(filename):
    return os.path.join(app.config['UPLOAD_FOLDER'], filename)
