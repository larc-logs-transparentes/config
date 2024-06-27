from requests import Response
from types import SimpleNamespace


class BUData:
    uf = ''
    zona = ''
    secao = ''
    id = ''
    meta = {}

    def __init__(self, uf, zona, secao):
        self.uf = uf
        self.zona = zona
        self.secao = secao


bu_list = [BUData("SP", 118, 1),
           BUData("SP", 118, 2),
           BUData("AM", 1, 616),
           BUData("AM", 1, 640),
           BUData("AM", 1, 641),
           BUData("AM", 1, 642),
           BUData("RS", 1, 1),
           BUData("RS", 1, 2),
           BUData("PB", 1, 1),
           BUData("PB", 1, 3),
           BUData("MT", 39, 364),
           BUData("MT", 39, 368),
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


