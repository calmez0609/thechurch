from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('rPzH0qSFLM093CZwNLrEw7FbzvyZh+LzSzk6nK9LCqzag+TgDcQenMPuW9AMLvBka79K4W/IYOo0K3B9R+Zm8as0KtX1THLS2tj44eHnfkWtZNJr7JvEjPfLaNtC/q3OJBgeqqUl1X2t8ISuQifrcgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6f1bcdf89caea3506ee178e114cb3fb2')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
def function(text):
    list=['路二四26:基督受這些害，又進入祂的榮耀，豈不是應當的麼?','約七39:耶穌這話是指着信入祂的人將要受的那靈說的；那時還沒有那靈，因爲耶穌尚未得酌着榮耀。']
    if text=='經結':
        text=random.choice(list)
    return text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(function(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
