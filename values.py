import requests
import json

'''
Currently, the value tracker is implemented using the Mavin.io API. https://api.mavin.io/docs/

Search takes a param q. For example, query = {'q':'Patrick Roy Montreal Canadiens 1986 Topps 53 PSA 9'}
'''


def get_keys():
    with open("sheet_info.json") as info_file:
        sheet_info = json.load(info_file)
    return sheet_info['mavin_api_key']


def search_for_values(search_terms):
    key = get_keys()
    query = {'q':search_terms}
    headers = {
        "x-api-key": key
    }

    response = requests.get(
        'https://api.mavin.io/search',
        headers=headers,
        params=query
    )

    if response.status_code != 200:
        return f"Error occurred in value search, status code {response.status_code}"
    else:
        return response.json()


def parse_json(value_json):
    pass  # TODO: parse values for report

# TODO: decide how to interface values script with menu
