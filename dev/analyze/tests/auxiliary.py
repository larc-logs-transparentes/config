from requests import Response
from types import SimpleNamespace


class BUData:
    turno:int = -1
    uf:str = ''
    zona:int = -1
    secao:int = -1
    eleicoes:list = []
    id = ''
    meta = {}

    def __init__(self, turno:int, uf:str, zona:int, secao:int, eleicoes:list):
        self.turno = turno
        self.uf = uf
        self.zona = zona
        self.secao = secao
        self.eleicoes = eleicoes


bu_list = [ # 1o turno
            BUData(1, "SP", 118, 1, [544, 546]),
            BUData(1, "SP", 118, 2, [544, 546]),
            BUData(1, "AM", 1, 616, [544, 546]),
            BUData(1, "AM", 1, 640, [544, 546]),
            BUData(1, "AM", 1, 641, [544, 546]),
            BUData(1, "AM", 1, 642, [544, 546]),
            BUData(1, "RS", 1, 1, [544, 546]),
            BUData(1, "RS", 1, 2, [544, 546]),
            BUData(1, "PB", 1, 1, [544, 546]),
            BUData(1, "PB", 1, 3, [544, 546]),
            BUData(1, "SC", 76, 68, [544, 546]),
            BUData(1, "SC", 95, 30, [544, 546]),
            BUData(1, "GO", 7, 3, [544, 546]),
            BUData(1, "GO", 7, 9, [544, 546]),
            # 2o turno
            BUData(2, "SP", 118, 1, [545, 547]),
            BUData(2, "SP", 118, 2, [545, 547]),
            BUData(2, "AM", 1, 616, [545, 547]),
            BUData(2, "AM", 1, 640, [545, 547]),
            BUData(2, "AM", 1, 641, [545, 547]),
            BUData(2, "AM", 1, 642, [545, 547]),
            BUData(2, "MT", 39, 364, [545]),
            BUData(2, "MT", 39, 368, [545]),
            BUData(2, "SC", 76, 68, [545, 547]),
            BUData(2, "SC", 95, 30, [545, 547]), 
            BUData(2, "GO", 7, 3, [545]), 
            BUData(2, "GO", 7, 9, [545]), 
          ]


def processar_response(resp:Response) -> tuple[str, object]:

    print(f"------\nurl  : {resp.url}\nhttp : {resp.status_code}")

    texto = resp.text
    print(f"texto: {texto}")

    try:
        json_obj = resp.json(object_hook=lambda d: SimpleNamespace(**d))
        print("json : presente")
    except Exception:
        json_obj = None
        print("json : ausente")

    return texto, json_obj


