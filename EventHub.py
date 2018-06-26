from azure.servicebus import ServiceBusService
import random
import json
import time
import datetime
from random import randint
import time
policy_name = 'myhubpllicy' # SharedAccessKeyName from Azure portal
policy_key = 'jIAsqcenXzgIkA1WuOe2ICVoeXqMim02UXUYZPGYnOo=' # SharedAccessKey from Azure portal
service_namespace='Your subriction name'
sbs = ServiceBusService(service_namespace,shared_access_key_name=policy_name,shared_access_key_value=policy_key)

for i in range(2000):
    time.sleep(0.60)
    print("inserting new record",i)
    # data = {'id': 'dev', 'timestamp': str(datetime.datetime.utcnow()), 'uv': random.random(), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100)}
    data = {
            'Date':str(datetime.datetime.utcnow()),   
            'Open': random.randint(120,200),   
            'High':  random.randint(120,200),   
            'Low': random.randint(120,200),   
            'Close': random.randint(120,200),   
            'Adj Close': random.randint(120,200),   
            'Volume': random.randint(2340,4000),  
            }
    print(data)
    s = json.dumps(data)
    sbs.send_event('myhub', s)#instance hub name.
