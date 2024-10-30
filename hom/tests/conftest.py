import pytest
import requests
import glob
from auxiliary import processar_response


@pytest.fixture(scope="session")
def my_setup(request):
    print ("Inicializando os testes.")
    bu_create_all()
    commit_all_trees()

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


def bu_create_all():
  folder:str = 'bus'
  bu_array = glob.glob("*-bu.dat", root_dir=folder)

  for bu in bu_array:
    bu_create(bu, folder)


def commit_all_trees():
  url = "http://127.0.0.1:9090/tree/commit-all-trees"

  payload = {}
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload)
  texto, result = processar_response(response)
  assert result.commited_trees
