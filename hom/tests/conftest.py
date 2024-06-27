import pytest
import requests
import glob
from auxiliary import processar_response


@pytest.fixture(scope="session")
def my_setup(request):
    print ("Inicializando os testes.")
    test_bu_create()
    test_commit_all_trees()

    def fin():
        print ("Finalizando os testes.")
    request.addfinalizer(fin)


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
