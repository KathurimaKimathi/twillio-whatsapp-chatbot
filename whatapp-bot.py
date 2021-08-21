from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    # add webhook logic here and return a response
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    message = resp.message()
    # responded is useful to track the case where the message does not include any of the keywords we are 
    # looking for, and in that case offer a generic response
    responded = False
    if 'quote' in incoming_msg:
        # returning a quote
        r = requests.get('https://api.quotable.io/random') #this url returns data in json format
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "Sorry, I am unable to retrieve quote at this time"
        message.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return different cat pictures
        message.media('https://cataas.com/cat')
        responded = True

    if not responded:
        message.body('Sorry, I only know about the quotes and cats')
    return str(resp)


if __name__ == '__main__':
    app.run()