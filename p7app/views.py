# coding: utf8
from config import *
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_logger import Logger
from flask_googlemaps import GoogleMaps
import requests
from .utils.google import *
from .utils.parser import *
app = Flask(__name__)

@app.route('/')
@app.route('/home/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/results', methods=["POST"])
def results():
    answer = {
        "message": {
            "raw_message": request.form["user_request_name"],
            "parsed_message": None
        },
        "google": None,
        "wikimedia": None,
        "error": {
            "has-error": None,
            "error_type": None
        }
    }

    answer["message"]["parsed_message"] = request_parser(answer["message"]["raw_message"])
    answer["google"] = get_data_from_google(answer["message"]["parsed_message"])
    return answer


if __name__ == "__main__":
    app.run(debug=True)
