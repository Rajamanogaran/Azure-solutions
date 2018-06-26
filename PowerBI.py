import requests
import json
from datetime import datetime
from random import randint
import time
import pymongo.mongo_client as client

url = "https://api.powerbi.com/beta/f3c7daf7-6e16-42e5-a785-979288092043/datasets/176f1b35-4c82-4776-8f14-7bc382317547/rows?key=fmULOQP55vIT2nDuzKZ2ZzTbKgAUsaxDHwJyY8TJJsZrO9fPiOO2MtVZuvtgIHO%2F4qx5SHb1nJ7bUd8g28QDxg%3D%3D"
try:
    for i in range(200):
        print(i)
        # date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        # print(date)
        data = [{ "ask": randint(1,200),"bid": randint(1,200),}]
        #print(json.dumps(data))
        r = requests.post(url, json.dumps(data), verify = False)
        print(r.status_code)
        print(r.reason)
except Exception as e:
    print(e)

#step1:before see this code you must create the powerbi stream dataset.
#step2:replace the your stream data url and your data in data variable.