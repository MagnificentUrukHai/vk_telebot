"""
Method for accessing vk_api is stored here

"""
import requests


def make_vk_api_request(cls, method, access_token=None, **kwargs):
    """Makes vk_api request"""
    parameters = {'v': '5.62'}
    if access_token:
        parameters['access_token'] = access_token
    if kwargs:
        for key in kwargs:
            parameters[key] = kwargs[key]
    response = requests.get('https://api.vk.com/method/{}.{}'.format(cls, method), params=parameters)
    return response
