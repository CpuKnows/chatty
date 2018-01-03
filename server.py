import warnings
import os
from flask import Flask, request

import chatbot
import messenger

app = Flask(__name__)

FACEBOOK_TOKEN = os.environ['FACEBOOK_TOKEN']
bot = None

@app.route('/', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token', '') == os.environ['FB_VERIFY_TOKEN']:
        return request.args.get('hub.challenge', '')
    else:
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data()
    for sender, message in messenger.messaging_events(payload):
        response = bot.respond_to(message)
        messenger.send_message(FACEBOOK_TOKEN, sender, response)

    return "ok"

bot = chatbot.Bot()
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
