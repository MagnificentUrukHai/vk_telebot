import requests
import os
import logging
from creds import bot_token

"""
Logger part
"""


def set_logger(path, name, *args, **kwargs):
    if not os.path.exists('./{}'.format(path)):
        os.makedirs(path)
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='./{}/{}_logger.log'.format(path, name),
                        format=LOG_FORMAT,
                        level=logging.DEBUG)
    return logging.getLogger(name)


def make_logfile_output(func):
    """
    Decorator function that will make
    other functions print DEBUG INFO in log file

    """

    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        message = result.url
        if bot_token in message:
            new_line = message.replace(bot_token, '<TOKEN>')
        logger.info(msg=new_line)
        return result

    return wrapped


"""
Bot part

"""


@make_logfile_output
def make_bot_request(method, *args, **kwargs):
    response = requests.get('https://api.telegram.org/bot{token}/{method}'.format(token=bot_token,
                                                                                  method=method), params=kwargs)
    # print(response.url)
    return response


def get_last_chatid_text(updates):
    last_update = updates[-1]
    return (last_update['message']['chat']['id'], last_update['message']['text'])


def send_message(chat_id, message):
    response = make_bot_request('sendMessage', chat_id=chat_id, text=message)
    return response


if __name__ == '__main__':
    logger = set_logger('logs', 'bot')
    updates = make_bot_request('getUpdates').json()['result']
    chat_id, text = get_last_chatid_text(updates)

    send_message(chat_id, text)
