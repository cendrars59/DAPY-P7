from config import *
from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/index/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_request = request.form["user_request_name"]
        return redirect(url_for("results", input_request=user_request))
    else:
        return render_template('index.html')



@app.route('/result/<input_request>')
def results(input_request):

    return render_template('result.html',
                           u_request=input_request)


if __name__ == "__main__":
    app.run(debug=True)
