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
            BUData(1, "SP", 1, 1, [619]),
            BUData(1, "SP", 1, 2, [619]),
            BUData(1, "SP", 1, 3, [619]),
            BUData(1, "BA", 1, 1, [619]),
            BUData(1, "BA", 1, 2, [619]),
            BUData(1, "BA", 1, 3, [619]),
            BUData(1, "RS", 1, 1, [619]),
            BUData(1, "RS", 1, 2, [619]),
            BUData(1, "RS", 1, 3, [619]),
            BUData(1, "AC", 1, 3, [619]),
            BUData(1, "AC", 1, 4, [619]),
            BUData(1, "AC", 1, 5, [619]),    

            # 2o turno
            BUData(2, "SP", 1, 1, [620]),
            BUData(2, "SP", 1, 2, [620]),
            BUData(2, "SP", 1, 3, [620]),
            BUData(2, "BA", 170, 1, [620]),
            BUData(2, "BA", 170, 1, [620]),
            BUData(1, "RS", 1, 1, [620]),
            BUData(1, "RS", 1, 2, [620]),
            BUData(1, "RS", 1, 3, [620]),

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


