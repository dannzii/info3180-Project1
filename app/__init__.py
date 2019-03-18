from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Xyuilo134dRTy"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ytisoywhqwyzsb:cf66f636aa2a3ab7427b0517d51033793e734953ca55612811194503733c1624@ec2-75-101-133-29.compute-1.amazonaws.com:5432/dcq1oq94gf9fa1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= './app/static/Images'


db = SQLAlchemy(app)

allowed_uploads = ['png', 'jpg', 'jpeg']


from app import views
