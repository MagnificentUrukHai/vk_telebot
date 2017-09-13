"""
This module makes authorisation

"""
import requests
import webbrowser
from creds import app_id

parameters = {
    'client_id': app_id,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'scope': ['groups'],
    'response_type': 'token',
    'v': '5.62',
    'state': '123456',
    'expires_in': 0
}

if __name__ == '__main__':
    resp = requests.get('https://oauth.vk.com/authorize', params=parameters)
    webbrowser.open(resp.url)
