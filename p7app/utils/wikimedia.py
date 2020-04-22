# coding: utf8
from config import *
from flask_logger import Logger
import requests


def get_data_from_wiki_media(user_request):
    """
    function to get data from google API in order to return address information according the incoming message
    :param user_request:
    :return: user_request
    """
    #Payload in order to get description and url according the returned lat & long from google API
    wiki_payload = {
        "action": "query",
        "format": "json",
        "prop": "links|extracts|info",
        "generator": "geosearch",
        "ggscoord": "{0}|{1}".format(user_request["google"]["result"]["geometry"]["location"]["lat"],
                                     user_request["google"]["result"]["geometry"]["location"]["lng"]),
        "gsradius": 1000,
        "gslimit": 10,
        "inprop": "url|preload",
        "exsentences": 4,
        "exintro": True
    }

    try:
        incoming_request = requests.post(WikiMediaUrl, params=wiki_payload)
        if incoming_request.status_code == 200:
            user_request["status"] = "OK"
            # get the lists of pages into the response
            list_of_pages = list(incoming_request.json()["query"]["pages"].keys())
            print(list_of_pages)
            # we set as answer only the first result if it exists
            if len(list_of_pages) != 0:
                user_request["wikimedia"] = incoming_request.json()["query"]["pages"][list_of_pages[0]]
                print(user_request["wikimedia"])
            else:
                user_request["status"] = "ZERO_RESULTS"
                user_request["errors"]["wikiAPI"] = True
        else:
            user_request["status"] = "NOK"
            user_request["errors"]["wikiAPI"] = True

    except requests.exceptions.RequestException as e:
        # this will log the whole traceback
        Logger.exception("call failed with %s", e)
        # here you either re-raise the exception, raise your own exception,
        # or return anything
        return None

    return user_request
