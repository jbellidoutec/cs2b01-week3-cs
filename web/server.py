from flask import Flask,render_template, request, session, Response, redirect
from database import connector
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/saludar')
def saludar():
    return "<h1>HOLA</h1>"


@app.route("/sumar/<n1>/<n2>")
def sumar(n1, n2):
    return str(int(n1)+int(n2))

@app.route('/authenticate', methods = ['POST'])
def authenticate():
    #Get data form request
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    print(username, password)
    if username == password:
        return json.dumps({"message":"si"})
    return json.dumps({"message":"fail"})

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
