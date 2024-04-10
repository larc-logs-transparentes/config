from requests import Response
from types import SimpleNamespace


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
