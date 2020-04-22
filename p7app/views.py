# coding: utf8
from flask import Flask, render_template, jsonify, request
from .utils.google import *
from .utils.parser import *
from .utils.wikimedia import *

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
    # If data have been received from Google maps API
    if answer["status"] == "OK":
        get_data_from_google(answer)
        if answer["status"] == "OK":
            get_data_from_wiki_media(answer)
    return jsonify(answer)


if __name__ == "__main__":
    app.run(debug=True)
