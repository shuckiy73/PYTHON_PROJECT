import requests
import json

response = requests.get('https://www.kufar.by/l/mebel')
mebel_data = response.text
data = mebel_data.split('title')
print()
