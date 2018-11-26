import telepot
from telepot.loop import MessageLoop
import os
import time
import json
telBot = telepot.Bot(os.environ.get('SLACK_BOT_TOKEN'))
import starterbot

from slackclient import SlackClient
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def print_msg(msg):
    print(json.dumps(msg, indent=10))

def on_chat(msg):
    print_msg(msg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    header = telepot.glance(msg, flavor="chat",long =True)
    slack_client.api_call(
        "chat.postMessage",
        channel = 'CEAFLPS1F',
        text = msg["text"]
    )
    print("send")
    

MessageLoop(telBot, {
    'chat': on_chat,
    #'callback_query': on_callback_query,
}).run_as_thread()

while(True):
    time.sleep(1)