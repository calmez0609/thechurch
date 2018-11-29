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
line_bot_api = LineBotApi('DuNPe+CYIv7cH5PqO8lp7a0S7+HsBf7g2L3i/aG6dNTjQLFoIcE0dhjdcrJlkG6tFb9KF3155ZvNcj159osT9SDdKY+q1iTQvy+AmeN+S2riPnP19mwH17TV1Wca1jzAjAyFKWyvn9iU1JGPtTusaQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9cd07218b8f805ec98f384d14b47ace7')

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
    list=['畜生','王八蛋','龜孫']
    if text=='隆基是':
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
