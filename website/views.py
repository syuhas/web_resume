from flask import Blueprint, render_template, request, url_for, redirect, session



views = Blueprint('views', __name__)



@views.route('/')
def home():
    """ if "userName" in session:
        return render_template('home.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('home.html')
    

@views.route('/projects')
def projects():
    """ if "userName" in session:
        return render_template('projects.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('projects.html')

    
@views.route('/resume')
def resume():
    """ if "userName" in session:
        return render_template('resume.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('resume.html')

@views.route('/project-site')
def project_site():
    """ if "userName" in session:
        return render_template('project-site.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('project-site.html')

@views.route('/project-cdk')
def project_cdk():
    """ if "userName" in session:
        return render_template('project-cdk.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('project-cdk.html')


@views.route('/colorchanger')
def test():
    """ if "userName" in session:
        return render_template('colorchanger.html', name=session['userName'])
    else:
        return redirect(url_for('views.login')) """
    return render_template('colorchanger.html')



""" @views.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['userName'] = request.form["nm"]
        session['email'] = request.form["em"]
        return redirect(url_for('views.user'))
    else:
        return render_template('login.html')


@views.route('/user')
def user():
    if "userName" and "email" in session:
        return render_template('home.html', name=session['userName'], eml=session['email'])
    else:
        return redirect(url_for('views.login'))

@views.route('/logout', methods=["POST", "GET"])
def logout():
    session.pop('userName', None)
    return redirect(url_for('views.login')) """


