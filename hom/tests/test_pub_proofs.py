import requests
from auxiliary import processar_response


def test_data_proof():
    url = "http://127.0.0.1:8080/tree/data-proof?tree_name=eleicao_546&index=2"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert response.status_code == 200
    assert result.status == 'ok'
    assert result.global_root
    assert result.local_tree
    assert result.local_tree.local_root.tree_name == 'eleicao_546'


def test_inclusion_proof():
    url = "http://127.0.0.1:8080/tree/inclusion-proof?tree_name=eleicao_546&index=2"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert response.status_code == 200
    assert result.status == 'ok'
    assert result.proof


def test_all_consistency_proof():
    url = "http://127.0.0.1:8080/tree/all-consistency-proof?tree_name=eleicao_546"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert response.status_code == 200
    assert result.status == 'ok'
    assert len(result.proofs) > 0
