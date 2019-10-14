import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return 'error no file'
    file = request.files['file']
    data = ''
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system("./convert.sh {} > /dev/null 2>&1".format(filename.replace(".webm","")))
        with open('output.txt', 'r') as file:
        	data = file.read().strip()
        	print(data) 
    return "{\"data\":\""+data+"\"}"

app.run(host='0.0.0.0', port=4444, debug=True)
