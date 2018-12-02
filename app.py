from flask import Flask, request, abort
import random
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
def function(text):
    list=['路二四:基督受這些害，又進入祂的榮耀，豈不是應當的麼?','約七39:耶穌這話是指着信入祂的人將要受的那靈說的；那時還沒有那靈，因爲耶穌尚未得着榮耀。','徒一8:但聖靈降臨在你們身上，你們就必得着能力，並要在耶路撒冷、猶太全地、撒瑪利亞，直到地極，作我的見證人。','林前一9:神是信實的，你們乃是爲牠所召，進入祂兒子我們主耶穌基督的交通。','希伯來書11:1:信是所望之事的質實，是未見之事的確證。']
    if text=='經節':
        text=random.choice(list)
    else:
        text=''
    return text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(function(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
