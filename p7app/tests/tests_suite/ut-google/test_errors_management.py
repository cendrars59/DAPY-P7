from p7app.utils import parser


dataset_search_error = {
        "messages": {
            "raw_message": "bbbbbbb  arc de triomphe ? rehghrgrghhreg",
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

# Test parser in nominal way
def test_google_error_search():
    reply = parser.request_parser(dataset_search_error)
    assert reply["status"] == "NOK"
    assert reply["errors"]["parser"] is None
    assert reply["errors"]["searchAPI"] is True
    assert reply["errors"]["resultsAPI"] is None