from unittest.mock import sentinel
from flask import Flask, json, jsonify, request
from Predict import predict
import requests
import ast
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! this is sentimental analysis api</p>"


@app.route("/<string:s>")
def called(s):
    print("s=", s, 'type= ', type(s))
    input_string = ast.literal_eval(s)
    print("inp_s=", input_string, 'type= ', type(input_string))
    res = predict(input_string)
    result = {

        "total_score": res[0],
        "negative_score": res[1],
        "positive_score": res[2],
        "sentence_list": input_string,
    }
    return jsonify(result)


@app.route('/', methods=['GET', 'POST'])
def create_row_in_gs():
    if request.method == 'POST':
        sentList = ast.literal_eval(request.args.get('sentList'))
        print('############')
        print(sentList)
        print('############')
        print('type= ', type(sentList))
        res = predict(sentList)
        result = {

            "total_score": res[0],
            "negative_score": res[1],
            "positive_score": res[2],
            "sentence_list": sentList,
        }
        return jsonify(result)
    else:
        return "<p>Please use proper API POST request call</p>"


if __name__ == '__main__':
    app.run(host="localhost", port=5500, debug=True)
