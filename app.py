from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('V8J6CcKNRsHZF9pVXzV02sTJ8pYQlU1B3kcXZZ1y9dlP4/QvNf2nWtwsyFLmrSTEgcgsV8Hn4W1RaGjkdQtrhWZK/QemcOwEHCK31GDj4mpkICb8OW5HRlZ3wYzXWWdJYz+Zb+mGxj9yDZW8N5tb4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fcd25fa436e9474a1213390b2e674ce3')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
