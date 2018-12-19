import configparser
from mastodon import Mastodon
from random import choice

config = configparser.ConfigParser()
config.read('config.ini')
MESSAGES_FILE = config['updates']['message_file']  # Contains all messages
RECENT_FILE = config['updates']['recent_file']   # Most recent message posted

mastodon = Mastodon(
    access_token=config['client']['access_token'],
    api_base_url=config['client']['api_base_url']
)


def select_message():
    with open(MESSAGES_FILE, 'r', encoding='UTF-8') as message, open(RECENT_FILE, 'w+', encoding='UTF-8') as recent:
        lines = message.readlines()
        status = choice(lines)
        while status in recent:
            status = choice(lines)
        recent.write(status)
        return status


def toot():  # A 'toot' is mastodon's version of a tweet or status post
    mastodon.status_post(select_message())


toot()
