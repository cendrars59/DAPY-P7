from p7app.utils import parser


# Test parser in nominal way
def test_parser_nominal_parser_message_with_adresse_key():
    dataset = {
        "messages": {
            "raw_message": "bbbbbbb adresse arc de triomphe ? rehghrgrghhreg",
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
    reply = parser.request_parser(dataset)
    assert reply["messages"]["parsed_message"] == " arc de triomphe "
    assert reply["status"] == "OK"
    assert reply["errors"]["parser"] is None


def test_parser_nominal_parser_message_with_trouve_key():
    dataset2 = {
        "messages": {
            "raw_message": "bbbbbbb où se trouve l'arc de triomphe ?"
                           "rehghrgrghhreg",
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
    reply = parser.request_parser(dataset2)
    assert reply["messages"]["parsed_message"] == " arc de triomphe "
    assert reply["status"] == "OK"
    assert reply["errors"]["parser"] is None


def test_parser_nominal_parser_message_without_question_tag():
    dataset3 = {
        "messages": {
            "raw_message": "bbbbbbb où se trouve l'arc de triomphe "
                           "rehghrgrghhreg",
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
    reply = parser.request_parser(dataset3)
    assert reply["messages"]["parsed_message"] == " arc de triomphe" \
                                                  " rehghrgrghhreg"
    assert reply["status"] == "OK"
    assert reply["errors"]["parser"] is None


# Test parser when the keyword adresse is missing
def test_parser_error_missing_add():
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
    reply = parser.request_parser(dataset_missing_ad)
    assert reply["messages"]["parsed_message"] == ""
    assert reply["status"] == "NOK"
    assert reply["errors"]["parser"] is True


def test_parser_missing_pattern():
    dataset_missing_pattern = {
        "messages": {
            "raw_message": "bbbbbbb  arc de triomphe  rehghrgrghhreg",
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
    reply = parser.request_parser(dataset_missing_pattern)
    assert reply["messages"]["parsed_message"] == ""
    assert reply["status"] == "NOK"
    assert reply["errors"]["parser"] is True

