import requests
from auxiliary import processar_response

def test_tree():
    url = "http://12   7.0.0.1:8080/tree?tree_name=global_tree"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"


def test_tree_root():
    url = "http://127.0.0.1:8080/tree/tree-root?tree_name=global_tree"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"


def test_all_roots_global_tree():
    url = "http://127.0.0.1:8080/tree/all-roots-global-tree"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"


def test_all_leaf_data_global_tree():
    url = "http://127.0.0.1:8080/tree/all-leaf-data-global-tree"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)
    assert result.status == "ok"

