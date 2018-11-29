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
line_bot_api = LineBotApi('V8J6CcKNRsHZF9pVXzV02sTJ8pYQlU1B3kcXZZ1y9dlP4/QvNf2nWtwsyFLmrSTEgcgsV8Hn4W1RaGjkdQtrhWZK/QemcOwEHCK31GDj4mpkICb8OW5HRlZ3wYzXWWdJYz+Zb+mGxj9yDZW8N5tb4QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fcd25fa436e9474a1213390b2e674ce3')

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text = Reply(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)

def Reply(text):
    if text == "hi" :
        return 'hello'

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
