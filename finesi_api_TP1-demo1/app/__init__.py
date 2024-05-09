from flask import Flask
from flask_cors import CORS
app = Flask(__name__, static_folder='Faces')
CORS(app)
# app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
app.config['UPLOAD_FOLDER'] = 'Faces'
app.config['SECRET_KEY'] = 'key_secret'
app.config['JWT_SECRET_KEY'] = 'ellanotequiere'
# app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
# app.config['JWT_QUERY_STRING_NAME'] = 'token'
from app import routes
