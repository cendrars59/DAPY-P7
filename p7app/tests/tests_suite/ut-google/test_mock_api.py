from p7app.utils.google import *
from requests import post
from io import BytesIO

def test_google_search_API(monkeypatch):
    pass
    results = {}

    class MockResponse:
        pass

    def mock_post(query):
        return MockResponse()

    monkeypatch.setattr('p7app.utils.google.request.post', mock_post)
