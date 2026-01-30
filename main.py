from cartolafc.api import Api
import os

def get_cartola():
    email = os.getenv("CARTOLA_EMAIL")
    senha = os.getenv("CARTOLA_SENHA")
    return Api(email=email, password=senha)

@app.get("/cartola-test")
def cartola_test():
    try:
        api = get_cartola()
        rodada = api.mercado().rodada_atual
        return {
            "login": "ok",
            "rodada_atual": rodada
        }
    except Exception as e:
        return {
            "login": "erro",
            "detalhe": str(e)
        }
