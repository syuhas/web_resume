from website import create_app
from flask import Flask


application = create_app()

if __name__ == '__main__':
    application.run(debug=True)

