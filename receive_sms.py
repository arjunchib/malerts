from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():

	# Take 1: Old SDK SMS - passed
	# resp = MessagingResponse()
	# resp.message("Hi, I'm MARTAN from mAlerts, here to give you your best rider experience!")
	# return str(resp)

	# Take 2: Simpler SMS - passed
	response = MessagingResponse()
	response.message("Hi, I'm MARTAN from mAlerts.")
	return str(response)

	# Take 3: MMS - failed (problem with MMS?)
	# response = MessagingResponse()
	# message = Message()
	# message.body("Hi, I'm Martan from mAlerts. If you need to refer to the MARTA map, I gotchu")
	# message.media("http://www.itsmarta.com/images/train-stations-map.jpg")
	# return str(response)


if __name__ == "__main__":
	app.run(debug=True)