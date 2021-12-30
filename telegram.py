import requests
import json
import configparser as cfg
from bot import chatbot

class telegram_chatbot():

    def __init__(self, config=None):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_msg(self, msg, chat_id):
        url = self.base + "sendMessage?text={}&chat_id={}".format(msg, chat_id)
        if msg is not None:
            requests.get(url)

bot = telegram_chatbot("config.cfg")

update_id = None
def make_reply(msg):
    reply = str(chatbot.get_response(msg))
    return reply
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            sender = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_msg(reply, sender)
            print('msg sent to, sender_id: ', sender)

