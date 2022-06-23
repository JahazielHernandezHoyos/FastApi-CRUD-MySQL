import requests
import json

# mandar en el header "Hola" a la url "http:127.0.0.1:8000/headers"


headers = {
    #comerede
    'Hola': '12312312312132'}
#camarada

r = requests.get('http://127.0.0.1:8000/headers', headers=headers)

#almacenar el resultado en una variable
#camarada

SAD
print(r.text)

