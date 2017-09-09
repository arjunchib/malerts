from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
	resp = MessagingResponse()

	resp.message("Hi, I'm MARTAN from mAlerts, here to give you your best rider experience!")

	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)