# pip install requests

import requests
import json

response = requests.get('https://api.sampleapis.com/coffee/hot')
coffe_data = json.loads(response.text)

for num, data in enumerate(coffe_data):
    print(f'{num}. {coffe_data}')
