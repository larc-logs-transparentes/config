import requests
from auxiliary import processar_response


def test_backend_public_online(my_setup):
    url = "http://127.0.0.1:8080/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.message == "Backend Executando"


def test_bu_service_online(my_setup):
    url = "http://127.0.0.1:9090/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.message == "Serviço de inserção de BU executando"


def test_tlmanager_online(my_setup):
    url = "http://127.0.0.1:8000/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"
