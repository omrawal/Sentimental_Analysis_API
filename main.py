from flask import Flask, json, jsonify
from Predict import predict
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# TODO change from string to list of strings


@app.route("/<string:s>")
def called(s):
    result = {
        "user_query": s,
        "chatbot_response": predict(s)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
