from flask import Flask,request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

app = Flask(__name__)

channel_secret = '0f0a9afab8d66c467aea84c5ce8622cd'
channel_access_token = 'bh01/sO9woN0YCQR7B/BhK/8UZmP+p/YI9izITvWFUWtBDRiLvXQdiJXiYMg7eMBRQ6Tco7+/CsuBRs4JBvZ4ZYSmEppOrKPa2J1T/JQSccbqJ2Pe/kA61SKONI+8+9KlCijSRq2sHczt4Lla5OG3gdB04t89/1O/w1cDnyilFU='

bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

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
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    bot_api.reply_message(
            event.reply_token,
            TextSendaMessage(text=event.message.text)
    )
if __name__ == "__main__":
    app.run(debug=True)
