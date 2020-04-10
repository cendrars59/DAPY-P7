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
        return render_template('index.html')
    else:
        return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)
