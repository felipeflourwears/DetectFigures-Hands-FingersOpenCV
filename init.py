import requests
import json

# URL del endpoint para enviar la solicitud POST
url = "https://go.plural.io/api/robots/message/0cd59285-0ea5-4f73-87d9-a779fa275daa"

# Token de autorización para la solicitud POST
token = "+eXDVVWxRKZ9n0OQfXxQhg5Y7b2aaGIuYNQN25cAP7M="


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + token  # Espacio después de 'Bearer'
}

# JSON con la estructura clave-valor
jsons = {"id": "0"}

response = requests.post(url, json=jsons, headers=headers)

# Comprobar el resultado de la solicitud
if response.status_code == 200:
    print("Solicitud exitosa!")
    print(response.json())
else:
    print("Error en la solicitud:", response.status_code)
