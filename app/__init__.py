from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Xyuilo134dRTy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uocggbmvbejqzt:39ab83c8fb36232ae847ca292ad5660b3b4861ec6dcfd41231ebaecc812d4b7b@ec2-54-197-232-203.compute-1.amazonaws.com:5432/d4ek4bjdpe2301'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= './app/static/Images'


db = SQLAlchemy(app)

allowed_uploads = ['png', 'jpg', 'jpeg']


from app import views
