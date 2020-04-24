# coding: utf8
import requests
from flask_logger import Logger

from config import GoogleDetailsUrl, GoogleSearchUrl, GoogleKey


def get_data_from_google_api(url, payload):
    """
    Function to request the different google API
    :param payload:
    :param url:
    :return: if sucess it returns a json message or log error message
    """
    try:
        incoming_request = requests.post(url, params=payload)
        return incoming_request.json()
    except requests.exceptions.RequestException as e:
        # this will log the whole traceback
        Logger.exception("call failed with %s", e)
        # here you either re-raise the exception, raise your own exception,
        # or return anything
        return None


def get_data_from_google(user_request):
    """
    function to get data from google API in order to return address information
     according the incoming message
    :param user_request:
    :return: user_request
    """
    query_payload = {
        "input": user_request["messages"]["parsed_message"],
        "inputtype": "textquery",
        "key": GoogleKey
    }
    search_result_json = get_data_from_google_api(GoogleSearchUrl,
                                                  query_payload)
    if search_result_json["status"] == "OK":
        existing_keys = search_result_json.keys()
        location = ""
        # selecting by default the first returned location
        if "results" in existing_keys and len(search_result_json["results"]) \
                != 0:
            location = search_result_json["results"][0]["place_id"]
        elif "candidates" in existing_keys and \
                len(search_result_json["candidates"]) != 0:
            location = search_result_json["candidates"][0]["place_id"]
        details_payload = {
            "place_id": location,
            "language": "fr",
            "key": GoogleKey
        }
        dataFromGoogle = get_data_from_google_api(GoogleDetailsUrl,
                                                  details_payload)
        if dataFromGoogle["status"] == "OK":
            user_request["status"] = "OK"
            user_request["google"] = dataFromGoogle
        # set error from results API
        else:
            user_request["status"] = "NOK"
            user_request["errors"]["resultsAPI"] = True
    # No results found by the API
    elif search_result_json["status"] == "ZERO_RESULTS":
        user_request["status"] = "ZERO_RESULTS"
    # set error from search API
    else:
        user_request["status"] = "NOK"
        user_request["errors"]["searchAPI"] = True

    return user_request
