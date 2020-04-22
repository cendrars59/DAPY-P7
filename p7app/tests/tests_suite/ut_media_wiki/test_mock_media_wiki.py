from p7app.utils.wikimedia import *
from config import *
from .data import *


# Mocking of Media queryAPI getting with results
def test_media_wiki_API_with_results(monkeypatch):

    payload = {
        "input": 'Mairie de Lille',
        "inputtype": "textquery",
        "key": GoogleKey
    }
    expected_results = {
                        "candidates": [
                                    {
                                        "place_id": "ChIJZR2qaYzVwkcRG74iJXu6kYc"
                                    }
                                        ],
                        "status": "OK"
                        }

    class MockMediaWikiApiResponse:
        def json(self):
            return expected_results

    # patching the post from requests
    def mock_requests_post(URL, params= payload):
        return MockMediaWikiApiResponse()

    monkeypatch.setattr('p7app.utils.wikimedia.requests.post', mock_requests_post)
    assert get_data_from_wiki_media(user_request) == expected_results

