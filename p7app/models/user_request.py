from p7app.utils.wikimedia import get_data_from_wiki_media
from p7app.utils.google import get_data_from_google
from p7app.utils.parser import request_parser


class UserRequest:

    def __init__(self, user_query):
        self.answer = {
                "messages": {
                    "raw_message": user_query,
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

    def return_answer_from_query(self):
        """
        Function returning answer populated after the differents APIs calls 
        :return:
        """
        request_parser(self.answer)
        # If data have been received from Google maps API
        if self.answer["status"] == "OK":
            get_data_from_google(self.answer)
            if self.answer["status"] == "OK":
                get_data_from_wiki_media(self.answer)
        return self.answer
