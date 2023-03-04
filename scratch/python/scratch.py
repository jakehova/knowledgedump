from vetext_incoming_forwarder_lambda import vetext_incoming_forwarder_lambda_handler, process_body_from_alb_invocation
import pytest
import http

albInvokeWithAddOn =  {'requestContext': {'elb': {'targetGroupArn': 'arn:aws-us-gov:elasticloadbalancing:us-gov-west-1:171875617347:targetgroup/prod-vetext-incoming-tg/235ef4ac03a4706b'}}, 'httpMethod': 'POST', 'path': '/twoway/vettext', 'queryStringParameters': {}, 'headers': {'accept': '*/*', 'connection': 'close', 'content-length': '574', 'content-type': 'application/x-www-form-urlencoded', 'host': 'api.va.gov', 'i-twilio-idempotency-token': 'edf7e44c-3116-4261-8ef6-e762ca6a4fce', 'user-agent': 'TwilioProxy/1.1', 'x-amzn-trace-id': 'Self=1-62d5ee4d-2cb5b7303f8e994a1f5cb6e1;Root=1-62d5ee4d-24b4119d5098534860221d75', 'x-forwarded-for': '3.89.199.39, 10.239.28.71, 3.89.199.39, 10.247.33.103', 'x-forwarded-host': 'api.va.gov:443', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https', 'x-forwarded-scheme': 'https', 'x-home-region': 'us1', 'x-real-ip': '3.89.199.39', 'x-twilio-signature': 'CRL6vBRyRo0DOLIud+zkNNjHi/Q='}, 'body': 'VG9Db3VudHJ5PVVTJlRvU3RhdGU9JlNtc01lc3NhZ2VTaWQ9U00wOGMwODNhYjY3YjRhNjdkOTYwZWU1ZTM1OTc2MDU5MyZOdW1NZWRpYT0wJlRvQ2l0eT0mRnJvbVppcD02OTE0MyZTbXNTaWQ9U00wOGMwODNhYjY3YjRhNjdkOTYwZWU1ZTM1OTc2MDU5MyZGcm9tU3RhdGU9TkUmU21zU3RhdHVzPXJlY2VpdmVkJkZyb21DaXR5PU5PUlRIK1BMQVRURSZCb2R5PVkxMyZGcm9tQ291bnRyeT1VUyZUbz01MzA3OSZNZXNzYWdpbmdTZXJ2aWNlU2lkPU1HYmU2YmIyN2E5Y2ExNWRlMjc2YzViODZmMGQ5ZTljMmUmVG9aaXA9JkFkZE9ucz0lN0IlMjJzdGF0dXMlMjIlM0ElMjJzdWNjZXNzZnVsJTIyJTJDJTIybWVzc2FnZSUyMiUzQW51bGwlMkMlMjJjb2RlJTIyJTNBbnVsbCUyQyUyMnJlc3VsdHMlMjIlM0ElN0IlN0QlN0QmTnVtU2VnbWVudHM9MSZSZWZlcnJhbE51bU1lZGlhPTAmTWVzc2FnZVNpZD1TTTA4YzA4M2FiNjdiNGE2N2Q5NjBlZTVlMzU5NzYwNTkzJkFjY291bnRTaWQ9QUM1NTFmYzYwODZmOTNhODM0OTI0NjZmYzYwNGM2OGFmNCZGcm9tPSUyQjEzMDg2NjA3NzgyJkFwaVZlcnNpb249MjAxMC0wNC0wMQ==', 'isBase64Encoded': True}
albInvokedWithoutAddOn = {'requestContext': {'elb': {'targetGroupArn': 'arn:aws-us-gov:elasticloadbalancing:us-gov-west-1:171875617347:targetgroup/prod-vetext-incoming-tg/235ef4ac03a4706b'}}, 'httpMethod': 'POST', 'path': '/twoway/vettext', 'queryStringParameters': {}, 'headers': {'accept': '*/*', 'connection': 'close', 'content-length': '573', 'content-type': 'application/x-www-form-urlencoded', 'host': 'api.va.gov', 'i-twilio-idempotency-token': '62c29575-5ed0-4638-92cb-297c5c8763ea', 'user-agent': 'TwilioProxy/1.1', 'x-amzn-trace-id': 'Self=1-62cda3f5-20dbbea14d3b70cf717c9a77;Root=1-62cda3f5-44e716a47645d83a41a7ee7f', 'x-forwarded-for': '44.202.129.169, 10.237.28.71, 44.202.129.169, 10.247.32.239', 'x-forwarded-host': 'api.va.gov:443', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https', 'x-forwarded-scheme': 'https', 'x-home-region': 'us1', 'x-real-ip': '44.202.129.169', 'x-twilio-signature': 'kvIT2C0P5KgiD+bCkzeUJcaIn4g='}, 'body': 'VG9Db3VudHJ5PVVTJlRvU3RhdGU9JlNtc01lc3NhZ2VTaWQ9U002NDI0Yjc5ZDY3NTlkYjU3MWI0OGUzMTZjYWVmNDlmMyZOdW1NZWRpYT0wJlRvQ2l0eT0mRnJvbVppcD05NjE1MCZTbXNTaWQ9U002NDI0Yjc5ZDY3NTlkYjU3MWI0OGUzMTZjYWVmNDlmMyZGcm9tU3RhdGU9TlYmU21zU3RhdHVzPXJlY2VpdmVkJkZyb21DaXR5PUNBUlNPTitDSVRZJkJvZHk9VkFYJkZyb21Db3VudHJ5PVVTJlRvPTgwNzI4Jk1lc3NhZ2luZ1NlcnZpY2VTaWQ9TUdmZWQ1NjhmMmQzZGM0YWM2ODUwYTBiYWQyYzk4NzNiMSZUb1ppcD0mQWRkT25zPSU3QiUyMnN0YXR1cyUyMiUzQSUyMnN1Y2Nlc3NmdWwlMjIlMkMlMjJtZXNzYWdlJTIyJTNBbnVsbCUyQyUyMmNvZGUlMjIlM0FudWxsJTJDJTIycmVzdWx0cyUyMiUzQSU3QiU3RCU3RCZOdW1TZWdtZW50cz0xJlJlZmVycmFsTnVtTWVkaWE9MCZNZXNzYWdlU2lkPVNNNjQyNGI3OWQ2NzU5ZGI1NzFiNDhlMzE2Y2FlZjQ5ZjMmQWNjb3VudFNpZD1BQzU1MWZjNjA4NmY5M2E4MzQ5MjQ2NmZjNjA0YzY4YWY0JkZyb209JTJCMTc3NTcyMDYwMjAmQXBpVmVyc2lvbj0yMDEwLTA0LTAx', 'isBase64Encoded': True}
sqsInvokedWithAddOn =  {'Records': [{'messageId': '143555b0-a74b-4793-8421-15cfeeaa487d', 'receiptHandle': 'AQEBfoQLBPET91yTrBH2AEToheRAt2X8vrQddfzr8CG4haD0LT+leMdW7uiDW9AEvr6YMbTVBgYNSBUegTU/g3KQ6deY1NqQxba+2j0KnHiiSrnzuotJAcSItGGjKh2kr4mxU/zg+WMmD1949uCS+og+x9Ayxy0762PtFiQ//vT1fiMVvCXtArDQHnj6p0ywENGq99TE/71UYXPn2WuuQcGgGvEi4kOYzz0u4/iQxH8kWz5u7Qroumob/4EVe7uAu6FCzSYylY+6yCHnDMCtqVKKndr1RP/hUiGkp/Cy8nZew2yh7lJvIIvi9hZjMi8/HQs8725HV1/83hOukYq8IrWIT0tDjDI49Xn/cOjzMGpbRmchr5tk4JOBM8Btg0JkkuM8Js7an5PiuvRS0sqeX1INTZQDCl7nOqNbPjqx0FKgDzg=', 'body': '{"ToCountry": "US", "SmsMessageSid": "SM031265e1d5c5e56c6243509a1eafc7e8", "NumMedia": "0", "FromZip": "74344", "SmsSid": "SM031265e1d5c5e56c6243509a1eafc7e8", "FromState": "OK", "SmsStatus": "received", "FromCity": "GROVE", "Body": "Y1", "FromCountry": "US", "To": "53079", "MessagingServiceSid": "MGbe6bb27a9ca15de276c5b86f0d9e9c2e", "NumSegments": "1", "ReferralNumMedia": "0", "MessageSid": "SM031265e1d5c5e56c6243509a1eafc7e8", "AccountSid": "AC551fc6086f93a83492466fc604c68af4", "From": "+19188015777", "ApiVersion": "2010-04-01"}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1658165878744', 'SenderId': 'AROASQBEVZJB7JNKLLQIY:project-prod-vetext-incoming-forwarder-lambda', 'ApproximateFirstReceiveTimestamp': '1658245723375'}, 'messageAttributes': {'source': {'stringValue': 'twilio', 'stringListValues': [], 'binaryListValues': [], 'dataType': 'String'}}, 'md5OfMessageAttributes': '54818a2ef8e5363fbdb8d318121ef7c4', 'md5OfBody': '63d3b9430c4741f41a20554ed655db1f', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws-us-gov:sqs:us-gov-west-1:171875617347:prod-vetext-failed-request-queue', 'awsRegion': 'us-gov-west-1'}]}

class HttpResponse:
  def __init__(self, status):
    self.status = status

@pytest.fixture
def http_success_response():
  return HttpResponse(200)

@pytest.fixture
def http_failure_response():
  return HttpResponse(500)

@pytest.mark.parametrize('event', [(albInvokedWithoutAddOn), (albInvokeWithAddOn)])
def test_verify_parsing_of_twilio_message(event):  
  response = process_body_from_alb_invocation(event)
  
  assert len(response) > 0
  assert 'AddOns' not in response

@pytest.mark.parametrize('event', [(albInvokedWithoutAddOn), (albInvokeWithAddOn), (sqsInvokedWithAddOn)])
def test_request_makes_vetext_call(mocker, http_success_response, event):
  vetext_mock = mocker.patch('vetext_incoming_forwarder_lambda.make_vetext_request', return_value=http_success_response)
  response = vetext_incoming_forwarder_lambda_handler(event, None)
  
  vetext_mock.assert_called_once()
  assert response['statusCode'] == 200