import requests
from auxiliary import processar_response

#----------------
url = "http://127.0.0.1:8080/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.message != "Backend Executando": exit(1)

#----------------
url = "http://127.0.0.1:9090/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.message != "Serviço de inserção de BU executando": exit(1)


#----------------
url = "http://127.0.0.1:8000/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.status != "ok": exit(1)

