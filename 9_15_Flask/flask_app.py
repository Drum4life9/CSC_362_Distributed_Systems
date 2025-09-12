import json

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    response = app.response_class(
        response=json.dumps("Hello there!"),
        status=200,
        mimetype='application/json'
    )
    return response