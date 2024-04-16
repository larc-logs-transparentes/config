import requests
from auxiliary import processar_response

def test_bu_create():
  url = "http://127.0.0.1:9090/bu/create"

  payload = {}
  files=[
    ('file',('o00407-0101500020065.bu',open(file='o00407-0101500020065.bu',mode='rb'),'application/octet-stream'))
  ]
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  texto, result = processar_response(response)
  assert result.status == "ok"


def test_commit_all_trees():
  url = "http://127.0.0.1:9090/tree/commit-all-trees"

  payload = {}
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload)
  texto, result = processar_response(response)
  assert result.commited_trees
