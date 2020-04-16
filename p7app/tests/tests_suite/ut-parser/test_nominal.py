from p7app.utils import parser


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


# Test parser in nominal way
def test_parser_nominal_parser_message():
    reply = parser.request_parser(dataset)
    assert reply["messages"]["raw_message"] == "bbbbbbb adresse arc de triomphe ? rehghrgrghhreg"
    assert reply["messages"]["parsed_message"] == "arc de triomphe "
    assert reply["status"] == "OK"
    assert reply["errors"]["parser"] is None






