from urllib.parse import parse_qsl
from base64 import b64decode

event = {
	"requestContext": {
		"elb": {
			"targetGroupArn": "arn:aws-us-gov:elasticloadbalancing:us-gov-east-1:642179902900:targetgroup/DELETEME-Lambda-tg/701827017b08d84d"
		}
	},
	"httpMethod": "POST",
	"path": "/twoway/vettext",
	"queryStringParameters": {},
	"headers": {
		"accept": "*/*",
		"connection": "close",
		"content-length": "423",
		"content-type": "application/x-www-form-urlencoded",
		"host": "varideshareccapi.architechturellc.com",
		"i-twilio-idempotency-token": "5236d77c-2d8f-44c2-8aba-bd39acf5f385",
		"user-agent": "TwilioProxy/1.1",
		"x-amzn-trace-id": "Root=1-626c5639-1f40237e3e9187554333c231",
		"x-forwarded-for": "3.92.28.28",
		"x-forwarded-port": "443",
		"x-forwarded-proto": "https",
		"x-home-region": "us1",
		"x-twilio-signature": "sv56/fI4AmU+p2K7XJDHU0HZj50="
	},
	"body": "VG9Db3VudHJ5PVVTJlRvU3RhdGU9Q08mU21zTWVzc2FnZVNpZD1TTTFkMDQxYTYyMzc4MTFhZDc1ZDU4YTdmOTk1YjU2NDg3Jk51bU1lZGlhPTAmVG9DaXR5PUFTUEVOJkZyb21aaXA9MjAxNjUmU21zU2lkPVNNMWQwNDFhNjIzNzgxMWFkNzVkNThhN2Y5OTViNTY0ODcmRnJvbVN0YXRlPVZBJlNtc1N0YXR1cz1yZWNlaXZlZCZGcm9tQ2l0eT1IRVJORE9OJkJvZHk9VGVzdCZGcm9tQ291bnRyeT1VUyZUbz0lMkIxOTcwMzAwNTY4MCZUb1ppcD04MTYxMSZOdW1TZWdtZW50cz0xJlJlZmVycmFsTnVtTWVkaWE9MCZNZXNzYWdlU2lkPVNNMWQwNDFhNjIzNzgxMWFkNzVkNThhN2Y5OTViNTY0ODcmQWNjb3VudFNpZD1BQ2IxYWEwMjNkZmY2NzYzMzIzMzIwMDZhNzc1YzFmOTE1JkZyb209JTJCMTcwMzkzMjc5NjkmQXBpVmVyc2lvbj0yMDEwLTA0LTAx",
	"isBase64Encoded": True
}
event_body_decoded = parse_qsl(b64decode(event["body"]).decode('utf-8'))
event_body = dict(event_body_decoded)

print(event_body.get("AccountSid", ""))