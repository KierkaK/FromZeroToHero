# To run server
# set FLASK_APP=lesson_1/mini_server.py
# flask run

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = 'Hello, World!!!'
    return response
