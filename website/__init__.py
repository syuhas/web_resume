from flask import Flask

def create_app():
    application = Flask(__name__)
    application.config['SECRET KEY'] = 'asdasdasd'

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix='/')
    """ application.register_blueprint(auth, url_prefix='/') """

    application.secret_key = '04241985'

    

    return application
