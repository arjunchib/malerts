from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC36f8a20c0d2f1b8d30bb5abdc3035997"
# Your Auth Token from twilio.com/console
auth_token  = "4385d9446189414082c7f9bf86566fb1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17064614889", 
    from_="+16787265889",
    body="Hi g money!")

print(message.sid)