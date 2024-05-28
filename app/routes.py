import os
from flask import request, redirect, url_for, send_from_directory, render_template, current_app as app, flash
from werkzeug.utils import secure_filename
from .storage import init_storage, save_file, get_files, get_file

@app.route('/')
def index():
    files = get_files()
    return render_template('upload_form.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        save_file(file, filename)
        flash('File successfully uploaded')
        return redirect(url_for('index'))

@app.route('/files/<filename>')
def uploaded_file(filename):
    path = '../upload-dir'

    return send_from_directory(path, filename)

init_storage()
