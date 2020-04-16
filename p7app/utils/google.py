# coding: utf8
from config import *
from flask_logger import Logger
import requests


def get_data_from_google_api(query):
    """
    Function to request the different google API
    :param query: built query according the requested service
    :return: if sucess it returns a json message or log error message
    """
    try:
        incoming_request = requests.post(query)
        return incoming_request.json()
    except requests.exceptions.RequestException as e:
        # this will log the whole traceback
        Logger.exception("call failed with %s", e)
        # here you either re-raise the exception, raise your own exception,
        # or return anything
        return None


def build_query_for_google_search(GoogleSearchUrl, input, GoogleKey):
    """
    Function to create the request for Google maps search API
    :return: string
    """
    return "{0}input={1}&inputtype=textquery&key={2}".format(GoogleSearchUrl,input, GoogleKey)


def build_query_for_google_details(GoogleDetailsUrl, input, GoogleKey):
    """
    Function to create the request for Google maps search API
    :return: string
    """
    return "{0}place_id={1}&language=fr&key={2}".format(GoogleDetailsUrl, input, GoogleKey)


def get_data_from_google(user_request):
    """
    function to get data from google API in order to return address information according the incoming message
    :param user_request:
    :return: user_request
    """
    query = build_query_for_google_search(GoogleSearchUrl, user_request["messages"]["parsed_message"], GoogleKey)
    search_result_json = get_data_from_google_api(query)
    if search_result_json["status"] == "OK":
        existing_keys = search_result_json.keys()
        location = ""
        if "results" in existing_keys and len(search_result_json["results"]) != 0:
            location = search_result_json["results"][0]["place_id"]
        elif "candidates" in existing_keys and len(search_result_json["candidates"]) != 0:
            location = search_result_json["candidates"][0]["place_id"]
        details_query = build_query_for_google_details(GoogleDetailsUrl, location, GoogleKey)
        dataFromGoogle = get_data_from_google_api(details_query)
        if dataFromGoogle["status"] == "OK":
            user_request["status"] = "OK"
            user_request["google"] = dataFromGoogle
        # set error from results API
        else:
            user_request["status"] = "NOK"
            user_request["errors"]["resultsAPI"] = True
    #No results found by the API
    elif search_result_json["status"] == "ZERO_RESULTS":
        user_request["status"] = "ZERO_RESULTS"
    #set error from search API
    else:
        user_request["status"] = "NOK"
        user_request["errors"]["searchAPI"] = True


    return user_request
