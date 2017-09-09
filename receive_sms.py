from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

app = Flask(__name__)
saidHello = False

@app.route("/", methods=['GET', 'POST'])
def sms_reply():

	# Take 1: Old SDK SMS - passed
	# resp = MessagingResponse()
	# resp.message("Hi, I'm MARTAN from mAlerts, here to give you your best rider experience!")
	# return str(resp)

	# Take 2: Simpler SMS - passed
	# response = MessagingResponse()
	# response.message("Hi, I'm MARTAN from mAlerts.")
	# return str(response)

	# Take 3: MMS - passed
	# response = MessagingResponse()
	# message = Message()
	# request_body = request.values.get("Body", None)
	# message.body("Hi, I'm Martan from mAlerts. If you need to refer to the MARTA map, I gotchu. You texted me: " + request_body)
	# message.media("http://www.itsmarta.com/images/train-stations-map.jpg")
	# response.append(message)
	# return str(response)

	global saidHello
	response = MessagingResponse()
	request_body = request.values.get("Body", None)

	lower_request_body = request_body.lower()
	stripped_request_body = lower_request_body.strip(",.!?/&-:;@'...")

	# waysToSayHi = ["hi", "hello", "hell", "howdy", "hh", "bonqour", "aloha", "hallo", "halo", "hey", "wassup", "wessup", "what is up", "whats up", "what's up", "hi there", "hithere", "yo"]
	# waysToSayTo = ["to", "two", "2"]

	# if (hi in stripped_request_body for hi in waysToSayHi):
	# 	print("Successful hi")
	# if (to in stripped_request_body for to in waysToSayTo):
	# 	print("Successful to")

	# ^ PROBLEM: successful to and successful hi being printed for literally every single line, thus simple if else

	# if someone says hi
	# if (not saidHello and hi in stripped_request_body for hi in waysToSayHi):
	# if ((not saidHello) and (hi in stripped_request_body for hi in waysToSayHi)):
	if (not saidHello):
		print("Saying hi")
		message = Message()
		message.body("Hi, I'm Martan from mAlerts! If you need a MARTA map, I gotchu. Please text me an origin and a destination. For example: Doraville to Midtown")
		message.media("http://www.itsmarta.com/images/train-stations-map.jpg")
		response.append(message)
		saidHello = True


	# once marten has said hello
	# elif (saidHello and to in stripped_request_body for to in waysToSayTo):
	else:
		print("Got origin and destination")
		message = Message()
		bodyArray = stripped_request_body.split(" ")

		if (not "to" in bodyArray):
			message.body("Hmm, you didn't use the right format... Please use the correct format and text me again.")
			response.append(message)
			return str(response)

		origin = bodyArray[0]
		destination = bodyArray[-1]
		message.body("Cool. So you're going from " + origin + " to " + destination + ". Let me check on that")
		response.append(message)


	return str(response)


if __name__ == "__main__":
	app.run(debug=True)