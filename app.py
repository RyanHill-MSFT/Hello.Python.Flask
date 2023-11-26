"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html')

@app.route('/files', methods=['GET'])
def get_files():
    """Renders a sample page."""
    return render_template('files.html')

@app.route('/files/process', methods=['POST'])
def process_files():
    file = request.files['file']
    app.config['UPLOAD_FOLDER']='.'  
    filename = secure_filename(file.filename)  
    path=os.path.join(app.config['UPLOAD_FOLDER'], filename)  
    file.save(path) 
    return render_template('files.html', message='File uploaded to ' + path)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
