from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    bio = db.Column(db.Text(300))
    created_on = db.Column(db.String(12))
    photo = db.Column(db.String(80))
    
    def __init__(self, first_name, last_name,gender,email,location,bio,created_on,photo):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.created_on = created_on
        self.photo = photo
        
        

    def __repr__(self):
        return "User: {0} {1}".format(self.firstname, self.lastname)