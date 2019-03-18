"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db, allowed_uploads
from flask import render_template, request, redirect, url_for, flash
from app.models import UserProfile
from app.forms import ProfileForm
from werkzeug.utils import secure_filename



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile", methods=["GET", "POST"])
def profile():
    newProfileForm = ProfileForm()
    
    if request.method == "POST":
        if newProfileForm.validate_on_submit():
            
            try:
                firstname = newProfileForm.firstname.data
                lastname = newProfileForm.lastname.data
                gender = newProfileForm.gender.data
                email = newProfileForm.email.data
                location = newProfileForm.location.data
                bio = newProfileForm.bibliography.data
                created = str(datetime.datetime.now()).split()[0]
                
                photo = newProfileForm.profilepic.data
                photo_name = secure_filename(photo.filename)
                
                user = UserProfile(firstname, lastname, gender, email, location, bio, created, photo_name)
                
                db.session.add(user)
                db.session.commit()
                
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
                flash("Profile Added", "success")
                return redirect(url_for("profiles"))
            
            except Exception as e:
                db.session.rollback()
                print(e)
                flash("Internal Error", "danger")
                return render_template("profile.html", form = newProfileForm)
        
        errors = form_errors(newProfileForm)
        flash(''.join(error+" " for error in errors), "danger")
    return render_template("profile.html", form = newProfileForm)


@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    profiles = []
    
    for user in users:
        profiles.append({"pro_pic": user.photo, "firstname":user.first_name, "lastname": user.last_name, "gender": user.gender, "location":user.location, "created_on":user.created_on, "id":user.id})
    
    return render_template("list-of-profiles.html", profiles = profiles)
    
@app.route('/profile/<userid>')
def inidi_profile(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    c_y = int(user.created_on.split("-")[0])
    c_m = int(user.created_on.split("-")[1])
    c_d = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(c_y, c_m, c_d)
    
    return render_template("view-created-profile.html", user = user)
    
def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")

def get_uploaded_images():
    uploads = []
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            if file.split('.')[-1] in allowed_uploads:
                uploads.append(file)

    return uploads
    
def form_errors(form):
    error_list =[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
            
    return error_list

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
