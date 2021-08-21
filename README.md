# twillio-whatsapp-chatbot
In this tutorial I’m going to to build a chatbot for WhatsApp using the Twilio API for WhatsApp and the Flask framework for Python.

It is a simple chatbot that recognizes two keywords in messages sent by the user and reacts to them. If the user writes anything that contains the word ``quote``, then the chatbot will return a random famous quote. If instead the message has the word ``cat``, then a random cat picture will be returned. If both ``quote`` and ``cat`` are present in the message, then the bot will respond with a quote and a cat picture together. :)

## How to run it
Create a new virtual environment by ``python3 -m venv your_env_name`` and install pip. Then install depedenties in requirements.txt file.

Then run the file ``python3 whatsapp-bot.py``. Thereafter, use ngtok to expose your application to the external internet. Type ``ngrok http 5000``. Copy the 'https' url and append `/bot` route at the end of the link and paste it in the webhook section in twillio programmable sms Whatsapp section.
