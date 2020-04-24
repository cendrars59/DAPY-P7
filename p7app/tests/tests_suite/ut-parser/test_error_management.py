from p7app.utils import parser


dataset_missing_ad = {
        "messages": {
            "raw_message": "bbbbbbb  arc de triomphe ? rehghrgrghhreg",
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

# Test parser when the keyword adresse is missing
def test_parser_error_missing_add():
    reply = parser.request_parser(dataset_missing_ad)
    assert reply["messages"]["raw_message"] == "bbbbbbb  arc de triomphe ? rehghrgrghhreg"
    assert reply["messages"]["parsed_message"] == ""
    assert reply["status"] == "NOK"
    assert reply["errors"]["parser"] is True

dataset_missing_question = {
        "messages": {
            "raw_message": "bbbbbbb adresse arc de triomphe  rehghrgrghhreg",
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

# Test parser when ? is missing
def test_parser_error_missing_question():
    reply = parser.request_parser(dataset_missing_question)
    assert reply["messages"]["raw_message"] == "bbbbbbb adresse arc de triomphe  rehghrgrghhreg"
    assert reply["messages"]["parsed_message"] == ""
    assert reply["status"] == "NOK"
    assert reply["errors"]["parser"] is True