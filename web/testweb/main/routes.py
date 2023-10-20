from flask import render_template, Blueprint, request, flash
import socket

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    # return render_template('home.html')
    return f"Container ID: {socket.gethostname()}"