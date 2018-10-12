from flask import Flask,request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
import json

app = Flask(__name__)

channel_secret = '0f0a9afab8d66c467aea84c5ce8622cd'
channel_access_token = 'bh01/sO9woN0YCQR7B/BhK/8UZmP+p/YI9izITvWFUWtBDRiLvXQdiJXiYMg7eMBRQ6Tco7+/CsuBRs4JBvZ4ZYSmEppOrKPa2J1T/JQSccbqJ2Pe/kA61SKONI+8+9KlCijSRq2sHczt4Lla5OG3gdB04t89/1O/w1cDnyilFU='

bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def command_list(text):
    cmd_list = open('data/command.txt')
    check = [line.strip() for line in cmd_list]
    for cmd in check:
        if(text.lower()==cmd):
            cmd_detail = open('data/{}.json'.format(cmd))
    data = json.load(cmd_detail)
    return data

@app.route("/")
def home():
    return "SUCCESS"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: {}".format(body))
    try:
        #events = parser.parse(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    profile = bot_api.get_profile(event.source.user_id)
    data = command_list(text)
    text_reply = "Nama: {0}\nDeskripsi: {1}\nPenggunaan: {2}".format(data['nama'],data['deskripsi'],data['penggunaan'])
    bot_api.reply_message(event.reply_token, TextSendMessage(text=text_reply))


if __name__ == "__main__":
    app.run(debug=True)
