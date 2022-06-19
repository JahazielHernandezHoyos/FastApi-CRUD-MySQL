import requests
import json

# mandar en el header "Hola" a la url "http:127.0.0.1:8000/headers"
headers = {'Hola': '12312312312132'}
r = requests.get('http://127.0.0.1:8000/headers', headers=headers)
print(r.text)

