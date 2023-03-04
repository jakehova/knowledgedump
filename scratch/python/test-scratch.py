import json 

print("go")
event ={'body': "{\"test\": \"value\"}"}
print("processing")
try: 
    json.loads(event.body)
    print("exception not hit")
except Exception as e:
    print("exception hit")