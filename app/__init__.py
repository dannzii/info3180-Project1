from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Xyuilo134dRTy"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project_1:dannzii@101@localhost/project_1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning



db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/Images'

app.config.from_object(__name__)
allowed_uploads = ['png', 'jpg', 'jpeg']
from app import views
