from flask import Flask
import pathlib

PROJECT_FOLDER = str(pathlib.Path(__file__).parent.parent.resolve())
UPLOAD_FOLDER = str(pathlib.Path(__file__).parent.parent.resolve())+'/Uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.api_key = "apikey123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROJECT_FOLDER'] = PROJECT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
