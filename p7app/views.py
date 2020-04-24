# coding: utf8
from flask import Flask, render_template, jsonify, request
from .models.user_request import UserRequest


app = Flask(__name__)


@app.route('/')
@app.route('/home/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/results', methods=["POST"])
def results():
    """
    Returning answer according the user request in json format
    :return:
    """
    return jsonify(UserRequest(request.form["user_request_name"]).
                   return_answer_from_query())


if __name__ == "__main__":
    app.run(debug=True)
