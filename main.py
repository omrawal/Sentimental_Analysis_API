from flask import Flask, json, jsonify
from Predict import predict
import ast
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<string:s>")
def called(s):
    print("s=", s)
    input_string = ast.literal_eval(s)
    print("inp_s=", input_string)
    result = {
        "score": predict(input_string),
        "sentence_list": input_string,
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
