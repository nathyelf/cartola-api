from fastapi import FastAPI
from cartolafc.api import Api
import os

# 🔴 PRIMEIRO: criar o app
app = FastAPI()

# 🔹 Função para obter a API do Cartola
def get_cartola():
    email = os.getenv("CARTOLA_EMAIL")
    senha = os.getenv("CARTOLA_SENHA")

    if not email or not senha:
        raise Exception("Variáveis de ambiente CARTOLA_EMAIL ou CARTOLA_SENHA não definidas")

    return Api(email=email, password=senha)

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
