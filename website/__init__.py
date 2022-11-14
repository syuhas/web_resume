from flask import Flask

def create_app():
    application = Flask(__name__)
    application.config['SECRET KEY'] = 'asdasdasd'

    from .views import views
    from .conn import conn

    application.register_blueprint(views, url_prefix='/')
    application.register_blueprint(conn, url_prefix='/')

    application.secret_key = '04241985'

    

    return application
