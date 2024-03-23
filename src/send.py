import http.client
import json
import ssl

# Define el cuerpo de la solicitud en formato JSON
data = {
    "name": "Simar Enrique Herrera Jimenez",
    "mail": "sehjud@gmail.com",
    "github_url": "https://github.com/simarhj/latam_challenge.git"
}

# Serializa los datos a formato JSON
json_data = json.dumps(data)

# Define la URL y el endpoint al que se enviará la solicitud POST
url = "advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app"
endpoint = "/data-engineer"

# Desactiva la verificación del certificado SSL
context = ssl._create_unverified_context()

# Establece la conexión con el servidor
conn = http.client.HTTPSConnection(url, context=context)

# Define las cabeceras de la solicitud
headers = {'Content-type': 'application/json'}

# Realiza la solicitud POST
conn.request("POST", endpoint, json_data, headers)

# Obtiene la respuesta del servidor
response = conn.getresponse()

# Lee y muestra la respuesta
print(response.read().decode())

# Cierra la conexión
conn.close()
