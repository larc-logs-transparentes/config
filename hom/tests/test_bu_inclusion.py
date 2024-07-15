import requests
import base64
from auxiliary import processar_response, bu_list, BUData
import tlverifier
import json


def test_bu_inclusion(my_setup):
    global_root = get_global_root()

    for bu_data in bu_list:

        for eleicao in bu_data.eleicoes:

            load_bu_id(bu_data, eleicao)
            bu_binary = base64.b64decode(bu_data.meta.bu.encode('ascii'))

            eleicao = bu_data.meta.merkletree_info.__dict__[str(eleicao)]
            print(f"\nEleição: {eleicao.tree_name} - index: {eleicao.index}")

            data_proof = get_tree_data_proof_dict(eleicao.tree_name, eleicao.index)
            # verify integrity of bu
            result = tlverifier.verify_data_entry(data_proof, global_root.value, bu_binary)

            assert result["success"] == True


def load_bu_id(bu_data:BUData, eleicao):
    url = f"http://localhost:8080/bu/find_by_info?UF={bu_data.uf}&zona={bu_data.zona}&secao={bu_data.secao}&id_eleicao={eleicao}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)

    assert len(result._id) > 0
    assert len(result.bu) > 0
    assert result.merkletree_info

    bu_data.id = result._id
    bu_data.meta = result


def get_global_root() -> object:
    url = "http://localhost:8080/tree/tree-root?tree_name=global_tree"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)

    assert result.status == 'ok'
    assert len(result.value) > 0

    return result


def get_tree_data_proof_dict(eleicao, index) -> dict:
    url = f"http://localhost:8080/tree/data-proof?tree_name={eleicao}&index={index}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    texto, result = processar_response(response)

    assert result.status == 'ok'
    assert result.global_root
    assert result.local_tree

    return json.loads(texto)
