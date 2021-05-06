from flask import Flask,render_template, request, session, Response, redirect
from database import connector
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/saludar')
def saludar():
    return render_template('/static/html/index.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
