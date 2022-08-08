from flask import Flask

def create_app():
    application = Flask(__name__, static_url_path='/static')
    application.config['SECRET KEY'] = 'asdasdasd'

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(auth, url_prefix='/')

    return application
