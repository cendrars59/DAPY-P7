from p7app.utils.google import *

dataset = {
        "messages": {
            "raw_message": "bbbbbbb adresse arc de triomphe ? rehghrgrghhreg",
            "parsed_message": "arc de triomphe "
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

def test_google_nominal():
    reply = get_data_from_google(dataset)
    assert reply["messages"]["raw_message"] == "bbbbbbb adresse arc de triomphe ? rehghrgrghhreg"
    assert reply["messages"]["parsed_message"] == "arc de triomphe "
    assert reply["status"] == "OK"
    assert reply["errors"]["searchAPI"] is None
    assert reply["errors"]["resultsAPI"] is None