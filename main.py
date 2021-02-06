import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask import Flask


from helper import (
    allowed_file
)


SECRET_KEY='something'


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp	
        file = request.files['file']
        if file.filename == '': 
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('dataset', secure_filename(filename)))
            resp = jsonify({'message' : 'File is successfully uploaded'})
            resp.status_code =201
            return resp
    
        else:
            resp = jsonify({'message' : 'Allowed file types are txt,pdf,png,jpg,jpeg'})
            resp.status_code = 400
            return resp

if __name__ == "__main__":
    app.run(debug= True)