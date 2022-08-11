from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')
    
@auth.route('/<usr>')
def user(usr):
    return render_template()
