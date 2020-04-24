# coding: utf8


def request_parser(incoming_message):
    """
    Function to retrieve the address from a raw message.
    Is considered as address any list of string between the string address
     and ?
    :param incoming_message: of type dictionary
    :return: a string value
    """

    words_in_incoming = incoming_message["messages"]["raw_message"].lower() \
        .split(" ")
    try:
        address_index = words_in_incoming.index("adresse")
        temp_address = words_in_incoming[address_index + 1:]
        try:
            question_mark_index = temp_address.index("?")
            address_list = temp_address[:question_mark_index]
            # The ? can not be just after the word adresse
            if question_mark_index > address_index + 1:
                for word in address_list:
                    incoming_message["messages"]["parsed_message"] += word + \
                                                                      " "
                    incoming_message["status"] = "OK"
            else:
                incoming_message["status"] = 'NOK'
                incoming_message["errors"]["parser"] = True
        except ValueError:
            incoming_message["status"] = 'NOK'
            incoming_message["errors"]["parser"] = True
    except ValueError:
        incoming_message["status"] = 'NOK'
        incoming_message["errors"]["parser"] = True

    return incoming_message
