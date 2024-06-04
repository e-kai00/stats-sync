from flask import Blueprint


profile = Blueprint('profile', __name__)

@profile.route('/profile')
def user_profile():
    return '<h1>Here is a page for User Profile</h>'