import requests
import glob
from auxiliary import processar_response


def test_backend_public_online():
    url = "http://127.0.0.1:8080/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.message == "Backend Executando"


def test_bu_service_online():
    url = "http://127.0.0.1:9090/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.message == "Serviço de inserção de BU executando"


def test_tlmanager_online():
    url = "http://127.0.0.1:8000/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"


# --------------------------------------
# ------- BU Service -------------------
# --------------------------------------

def bu_create(bu_name:str, folder:str):
  url = "http://127.0.0.1:9090/bu/create"

  payload = {}
  files=[
    ('file',(bu_name,open(file=f'{folder}/{bu_name}',mode='rb'),'application/octet-stream'))
  ]
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  texto, result = processar_response(response)
  assert result.status == "ok"


def test_bu_create():
  folder:str = 'bus'
  bu_array = glob.glob("*.bu", root_dir=folder)

  for bu in bu_array:
    bu_create(bu, folder)


def test_commit_all_trees():
  url = "http://127.0.0.1:9090/tree/commit-all-trees"

  payload = {}
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload)
  texto, result = processar_response(response)
  assert result.commited_trees
