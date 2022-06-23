import requests
import json

# mandar en el header "Hola" a la url "http:127.0.0.1:8000/headers"
<<<<<<< HEAD
headers = {'Hola': '12312312312132'
}
=======


headers = {
    #comerede
    'Hola': '12312312312132'
    }
#camarada

>>>>>>> 17ff15c9887e69f723154565f5cae35514a71419
r = requests.get('http://127.0.0.1:8000/headers', headers=headers)


print(r.text)

# mandar en el header "Hola" a la url "http:
