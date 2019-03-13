"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db, login_manager, allowed_uploads
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from .forms import ContactForm
from werkzeug.utils import secure_filename



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile",  methods=["GET", "POST"])
def profile():
    myform = ContactForm()
    if request.method == 'POST':
        if myform.validate_on_submit():
            F_name = myform.firstname.data
            L_name = myform.lastname.data
            Gender = myform.gender.data
            Email = myform.email.data
            Location = myform.location.data
            Bibliography = myform.bibliography.data
            Created = str(datetime.datetime.now()).split()[0]
           
            Profilepic = myform.profilepic.data
            filename = secure_filename(Profilepic.filename)
            Profilepic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            user = UserProfile(F_name, L_name, Gender, Email, Location, Bibliography, Created, Profilepic)
            
            
            flash('Your profile has successfully been created', 'success')
            return redirect(url_for('home'))
        else:
            
            flash("OOOPS Sorry something went worng, Try again")
    return render_template('profile.html', form=myform )

def get_uploaded_images():
    uploads = []
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            if file.split('.')[-1] in allowed_uploads:
                uploads.append(file)

    return uploads

@app.route('/secure-page')
@login_required
def secure():
    return render_template('secure.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
