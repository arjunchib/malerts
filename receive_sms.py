from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
# from difflib import SequenceMatcher
from difflib import get_close_matches
from stations import getStationsDict

# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():

	stationsOld = set([
		"North Springs", "Sandy Springs", "Dunwoody", "Medical Center", "Buckhead", "Lindbergh Center", "Arts Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "West End", "Oakland City", "Lakewood/Ft. McPherson", "East Point", "College Park", "Airport",
		"Doraville", "Chamblee", "Brookhaven/Oglethorpe", "Lenox", "Lindbergh Center", "Arts Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "West End", "Oakland City", "Lakewood/Ft. McPherson", "East Point", "College Park", "Airport",
		"Bankhead", "Ashby", "Vine City", "Dome/GWCC/Philips Arena/CNN Center", "Five Points", "Georgia State", "King Memorial", "Inman Park/Reynoldstown", "Edgewood/Candler Park",
		"Hamilton E. Holmes", "West Lake", "Ashby", "Vine City", "Dome/GWCC/Philips Arena/CNN Center", "Five Points", "Georgia State", "King Memorial", "Inman Park/Reynoldstown", "Edgewood/Candler Park", "East Lake", "Decatur", "Avondale", "Kensington", "Indian Creek"
	])
	stationsOld = list(stationsOld)
	stations = []
	for i in stationsOld:
		i = i.lower()
		stations.append(i)


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

	response = MessagingResponse()
	message = Message()
	request_body = request.values.get("Body", None)
	lower_request_body = request_body.lower()
	stripped_request_body = lower_request_body.strip(",.!?/&-:;@'...")
	bodyArray = stripped_request_body.split(" ")
	print(stripped_request_body)

	waysToSayHi = ["hi", "hello", "hell", "howdy", "hh", "bonqour", "aloha", "hallo", "halo", "hey", "wassup", "wessup", "what is up", "whats up", "what's up", "hi there", "hithere", "yo", "sup"]

	# if text says "hi" or similar, similar() must return 90% or 0.9
	# if (similar(stripped_request_body, hi) >= 0.9 for hi in waysToSayHi):
	# if (hi in bodyArray[0] for hi in waysToSayHi): <-- one line for loop did not work

	# checks to see if hi or similar is in text
	for hi in waysToSayHi:
		if hi in bodyArray:
			print("Text says hi")
			message.body("Hi, I'm Martan from mAlerts! If you need a MARTA map, I got you. Please text me an origin and a destination. For example: Doraville to Midtown")
			message.media("http://www.itsmarta.com/images/train-stations-map.jpg")
			response.append(message)
			return str(response)

	# if text says "<station> to <station>""
	if ("to" in bodyArray):
		print("Text says <station> to <station>")

		toIndex = bodyArray.index("to")
		origin = ' '.join(bodyArray[0:toIndex])
		destination = ' '.join(bodyArray[toIndex+1:])

		stationsDict = getStationsDict()
		keys = stationsDict.keys()

		originFinalKeyList = get_close_matches(origin, keys, 1)
		destinationFinalKeyList = get_close_matches(destination, keys, 1)

		# if text contains "to" but does not contain valid station names
		if (len(originFinalKeyList) == 0 or len(destinationFinalKeyList) == 0):
			print("Text contains to but not valid station names")
			message.body("Hmm, you didn't use the right format... Please text me a valid origin and a destination. For example: Doraville to Midtown")
			response.append(message)
			return str(response)

		originFinalKey = originFinalKeyList[0]
		destinationFinalKey = destinationFinalKeyList[0]

		finalOrigin = stationsDict[originFinalKey]
		finalDestination = stationsDict[destinationFinalKey]
			
		message.body("Cool. So you're going from " + finalOrigin + " to " + finalDestination + ". Let me check on that!")
		response.append(message)

	# if text says something invalid
	else:
		message.body("Hey, it looks like you said something not valid! Just send me a hello or your origin and destination stations. For example: Doraville to Midtown")


	return str(response)


if __name__ == "__main__":
	app.run(debug=True)