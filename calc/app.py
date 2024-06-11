# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def adding():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))

@app.route('/sub')
def subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))

@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))

@app.route('/div')
def dividing():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))

