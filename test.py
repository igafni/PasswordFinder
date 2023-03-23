import requests
import json

texts = ["""The secret password for the production server is: HalaMadrid2

Please don’t tell anyone on the production team that the other password is RealMadrid12 . This is our backup. 

or
Mori1324

(jsnfjn.76>?&?>##&?&%#%&?)
This is a test document to illustrate password extraction.
"""]
data = json.dumps({"texts": texts})
res = requests.post(r"http://172.17.128.1:8080/api/passwords", data=data)
print(res.json())
