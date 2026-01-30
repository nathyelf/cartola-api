from fastapi import FastAPI
from cartolafc.api import Api
import os

app = FastAPI()

def get_cartola():
    email = os.getenv("CARTOLA_EMAIL")
    senha = os.getenv("CARTOLA_SENHA")

    if not email or not senha:
        raise Exception("Variáveis de ambiente CARTOLA_EMAIL ou CARTOLA_SENHA não definidas")

    api = Api()
    api.login(email, senha)   # ✅ JEITO CERTO AGORA
    return api

@app.get("/")
def root():
    return {"status": "API ONLINE"}

@app.get("/liga/{slug}")
def liga_teste(slug: str):
    return {"ok": True, "slug_recebido": slug}

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


# 🔹 Endpoint raiz
@app.get("/")
def root():
    return {"status": "API ONLINE"}

# 🔹 Endpoint de teste simples
@app.get("/liga/{slug}")
def liga_teste(slug: str):
    return {
        "ok": True,
        "slug_recebido": slug
    }

# 🔹 Endpoint para testar login no Cartola
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
