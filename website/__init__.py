from flask import Flask

def create_app():
    application = Flask(__name__, static_url_path='/static')
    application.config['SECRET KEY'] = 'asdasdasd'

    from .views import views

    application.register_blueprint(views, url_prefix='/')

    return application
