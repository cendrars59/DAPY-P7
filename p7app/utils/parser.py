# coding: utf8
import re


def request_parser(incoming_message):
    """
    Function to retrieve the address from a raw message.
    Is considered as address any list of string between the string address
     and ?
    :param incoming_message: of type dictionary
    :return: incoming_message
    """

    # Regex searching the following pattern. The location est between
    # the words adresse or où se trouve and ?
    regex = "(?<=adresse)[\w\s]{1,}[^\?]|(?<=où se trouve)[\w\s]{1,}[^\?]"
    words_in_incoming = incoming_message["messages"]["raw_message"].lower(). \
        replace("d'", "").replace("l'", "")
    print(words_in_incoming)
    try:
        matching = re.search(r'{0}'.format(regex), words_in_incoming)
        if matching is not None:
            incoming_message["messages"]["parsed_message"] = matching.group(0)
            incoming_message["status"] = "OK"

        # No match found according pattern
        else:
            incoming_message["status"] = 'NOK'
            incoming_message["errors"]["parser"] = True
    # The pattern can not be applied
    except ValueError:
        incoming_message["status"] = 'NOK'
        incoming_message["errors"]["parser"] = True

    return incoming_message
