from vk_api import make_vk_api_request
from creds import access_token
import json


def form_search_result_list(keyword, sort):
    id_list = []
    response = make_vk_api_request('groups', 'search', access_token, q=keyword, sort=sort).json()
    for item in response['response']['items']:
        id_list.append(dict(id=item['id'], name=item['name']))
    return id_list


def pop_irrelevant_results(id_list):
    irrelevant_word_list = [
        'домашнее задание', 'помощь',
        'подготовка', 'решить', 'монти',
        'пайтон', 'быстро', 'сумки', 'изделия'
    ]
    for item in id_list:
        for word in irrelevant_word_list:
            if word in item['name'].lower():
                id_list.remove(item)
                break
    return id_list


def make_search_data_json_file(filename, keyword, sort):
    with open(filename, 'w') as file:
        data_to_write = pop_irrelevant_results(form_search_result_list(keyword, sort))
        json.dump(data_to_write, file, indent=4, sort_keys=True, separators=(',', ':'))


if __name__ == '__main__':
    make_search_data_json_file('db.json', 'python', 5)
