# coding: utf8
from config import *
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_logger import Logger
import requests


def get_data_from_wiki_media(user_request):
    """
    function to get data from google API in order to return address information according the incoming message
    :param user_request:
    :return: user_request
    """
    query = "{0}action=query&generator=geosearch&ggscoord={1}|{2}&prop:coordinates|pageimages&format=json".format(WikiMediaUrl,
                                                                          user_request["google"]["result"]
                                                                          ["geometry"]["location"]["lat"],
                                                                          user_request["google"]["result"]
                                                                          ["geometry"]["location"]["lng"])
    try:
        incoming_request = requests.post(query)
        print(incoming_request.json())
        if incoming_request.status_code == 200:
            return incoming_request.json()
    except requests.exceptions.RequestException as e:
        # this will log the whole traceback
        Logger.exception("call failed with %s", e)
        # here you either re-raise the exception, raise your own exception,
        # or return anything
        return None

    # return user_request