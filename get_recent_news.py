"""
I don't know what exactly this module does

"""
from vk_api import make_vk_api_request
from creds import access_token
import json


def load_json_data_from_file(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def get_id_list(json_data):
    id_list = []
    for item in json_data:
        id_list.append(dict(id=item['id']))
    return id_list


def get_news(filename):
    kwargs = {
        'extended': 1,
        'groups': get_id_list(load_json_data_from_file(filename))
    }
    response = make_vk_api_request('newsfeed', 'search', access_token, **kwargs)
    return response.json()


if __name__ == '__main__':
    print(get_news('db.json'))
