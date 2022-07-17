
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def default():

    return jsonify({"status" : "200", "message" : "Hey there, happy hacking..."})