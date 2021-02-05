
#!/usr/bin/python -tt
import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask import Flask

UPLOAD_FOLDER = 'c:/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadfiles', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp	
        file = request.files('file[]')
        if file.filename == '': 
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message' : 'File is successfully uploaded'})
            resp.status_code =201
            return resp
    
        else:
            resp = jsonify({'message' : 'Allowed file types are txt,pdf,png,jpg,jpeg'})
            resp.status_code = 400
            return resp
    

if __name__ == "__main__":
    app.run(debug= True)
