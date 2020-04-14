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
        "messages": {
            "raw_message": request.form["user_request_name"],
            "parsed_message": ""
        },
        "google": None,
        "wikimedia": None,
        "status": None,
        "errors": {
            "parser": None,
            "searchAPI": None,
            "resultsAPI": None,
            "wikiAPI": None
        }
    }

    request_parser(answer)
    if answer["status"] == "OK":
        get_data_from_google(answer)

    return jsonify(answer)


if __name__ == "__main__":
    app.run(debug=True)
