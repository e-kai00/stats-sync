from flask import Blueprint


exp_app = Blueprint('exp_app', __name__)

@exp_app.route('/')
def index():
    return '<h1>Welcome to my Home Page</h1>'