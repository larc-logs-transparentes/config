import requests
from auxiliary import processar_response

#------
url = "http://127.0.0.1:8080/tree?tree_name=global_tree"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.status != "ok": exit(1)

#------
url = "http://127.0.0.1:8080/tree/tree-root?tree_name=global_tree"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.status != "ok": exit(1)

#-----
url = "http://127.0.0.1:8080/tree/all-roots-global-tree"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.status != "ok": exit(1)

#----
url = "http://127.0.0.1:8080/tree/all-leaf-data-global-tree"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
texto, result = processar_response(response)
if result.status != "ok": exit(1)

