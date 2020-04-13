# coding: utf8


def request_parser(incoming_request):
    """
    Function to retrieve the address from a raw message.
    Is considered as address any list of string between the string address and ?
    :param incoming_request:
    :return: a string value
    """
    words_in_incoming = incoming_request.split(" ")
    print(words_in_incoming)
    try:
       address_index = words_in_incoming.index("adresse")
       print(address_index)
       temp_address = words_in_incoming[address_index + 1:]
       print(temp_address)
       try:
           question_mark_index = temp_address.index("?")
           print(question_mark_index)
           address_list = temp_address[:question_mark_index]
           address = ""
           for word in  address_list:
               address+= word+" "
           print(address)
           return address
       except ValueError:
           question_mark_index = None
           return "Parser error"
    except ValueError:
        address_index = None
        return "Parser error"


