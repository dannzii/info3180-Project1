from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from . import allowed_uploads


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField ('Geneder', choices = [("None", "Select Gender"),('male','Male'), ('female','Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    bibliography = TextAreaField('Bibliography', validators=[DataRequired()])
    profilepic = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(allowed_uploads, ''.join( item+" " for item in allowed_uploads)+"only")
    ])
    
