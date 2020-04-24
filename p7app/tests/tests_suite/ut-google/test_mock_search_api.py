from p7app.utils.google import get_data_from_google_api
from config import *


URL = GoogleSearchUrl

# Mocking of Google search API getting with results
def test_google_search_API_with_results(monkeypatch):

    query_payload = {
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

    class MockGoogleApiResponse():
        def json(self):
            return expected_results

    # patching the post from requests
    def mock_requests_post(URL, params= query_payload):
        return MockGoogleApiResponse()

    monkeypatch.setattr('p7app.utils.google.requests.post', mock_requests_post)
    assert get_data_from_google_api(URL, query_payload) == expected_results


# Mocking of Google search API getting with results
def test_google_search_API_with_no_results(monkeypatch):
    query_payload = {
        "input": 'aaaaaaa',
        "inputtype": "textquery",
        "key": GoogleKey
    }
    expected_results = {
                        "candidates": [],
                        "status": "ZERO_RESULTS"
                        }

    class MockGoogleApiResponse:
        def json(self):
            return expected_results

    def mock_requests_post(URL, params=query_payload):
        return MockGoogleApiResponse()

    monkeypatch.setattr('p7app.utils.google.requests.post', mock_requests_post)
    assert get_data_from_google_api(URL, query_payload) == expected_results