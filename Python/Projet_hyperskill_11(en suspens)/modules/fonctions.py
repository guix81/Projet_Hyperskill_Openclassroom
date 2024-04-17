import requests
import json


while True:
    print('Input the URL:')
    req = requests.get("http://api.quotable.io/quotes/-4WQ_JwFWI")
    #req = requests.get(input())
    if req.status_code == 200:
        y = json.loads(req.content)
        print(y["content"])
        break
    else:
        print('Invalid quote resource!')
        break