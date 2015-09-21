"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file return_message.py
File to define default return messages
"""


def return_message(self, status_code):
    """Return a dict with the status code and messages."""
    return_message = ''

    if status_code == 200:
        return_message = 'Everything Worked.'
        response = {}

        response['status_code'] = status_code
        response['return_message'] = return_message

    elif status_code == 201:
        return_message = 'Successfully Created.'
        response = {}

        response['status_code'] = status_code
        response['return_message'] = return_message

    elif status_code == 404:
        return_message = 'Not Found.'
        response = {}

        response['status_code'] = status_code
        response['return_message'] = return_message

    elif status_code == 500:
        return_message = 'Iternal Server Error.'
        response = {}

        response['status_code'] = status_code
        response['return_message'] = return_message

    else:
        return_message = 'Something went wrong.'
        response = {}

        response['status_code'] = status_code
        response['return_message'] = return_message

    return response
