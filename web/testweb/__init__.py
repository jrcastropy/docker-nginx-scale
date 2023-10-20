from flask import Flask, flash, redirect

def create_app():

    app = Flask(__name__)
    app.secret_key = 'testwebapp'
    from testweb.main.routes import main
    app.register_blueprint(main)

    return app