from flask import Blueprint, render_template

import botocore

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/projects')
def projects():
    return render_template('projects.html')

    
@views.route('/resume')
def resume():
    return render_template('resume.html')

@views.route('/project-site')
def project_site():
    return render_template('project-site.html')

@views.route('/project-cdk')
def project_cdk():
    return render_template('project-cdk.html')

