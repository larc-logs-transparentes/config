import requests
from auxiliary import processar_response


#-------
url = "http://127.0.0.1:8080/tree/data-proof?tree_name=teste_545&index=2"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if response.status_code != 200: exit(1)

#-------
url = "http://127.0.0.1:8080/tree/inclusion-proof?tree_name=teste_545&index=2"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if response.status_code != 200: exit(1)

#-------
url = "http://127.0.0.1:8080/tree/all-consistency-proof?tree_name=teste_545"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if response.status_code != 200: exit(1)
