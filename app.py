<<<<<<< HEAD
from fastapi import FastAPI
from cartolafc.api import Api
import os
import time

app = FastAPI()

# ===== CACHE SIMPLES =====
CACHE = {}
CACHE_TTL = 1800  # 30 minutos

def cache_valido(chave):
    return chave in CACHE and time.time() - CACHE[chave]["time"] < CACHE_TTL

def set_cache(chave, dados):
    CACHE[chave] = {"time": time.time(), "dados": dados}


def get_api():
    return Api(
        email=os.getenv("CARTOLA_EMAIL"),
        password=os.getenv("CARTOLA_SENHA")
    )

@app.get("/")
def root():
    return {"status": "API Cartola ONLINE"}

# ===== BUSCAR LIGA =====
@app.get("/liga/{slug}")
def liga(slug: str):
    if cache_valido(slug):
        return CACHE[slug]["dados"]

    api = get_api()
    liga = api.league(slug=slug)
    ranking = api.league_ranking(liga.liga_id)

    dados = {
        "liga": liga.nome,
        "times": [
            {
                "posicao": r.rank,
                "time": r.time_nome,
                "pontos": r.pontos
            }
            for r in ranking
        ]
    }

    set_cache(slug, dados)
    return dados
=======
from fastapi import FastAPI
from cartolafc.api import Api
import os
import time

app = FastAPI()

# ===== CACHE SIMPLES =====
CACHE = {}
CACHE_TTL = 1800  # 30 minutos

def cache_valido(chave):
    return chave in CACHE and time.time() - CACHE[chave]["time"] < CACHE_TTL

def set_cache(chave, dados):
    CACHE[chave] = {"time": time.time(), "dados": dados}


def get_api():
    return Api(
        email=os.getenv("CARTOLA_EMAIL"),
        password=os.getenv("CARTOLA_SENHA")
    )

@app.get("/")
def root():
    return {"status": "API Cartola ONLINE"}

# ===== BUSCAR LIGA =====
@app.get("/liga/{slug}")
def liga(slug: str):
    if cache_valido(slug):
        return CACHE[slug]["dados"]

    api = get_api()
    liga = api.league(slug=slug)
    ranking = api.league_ranking(liga.liga_id)

    dados = {
        "liga": liga.nome,
        "times": [
            {
                "posicao": r.rank,
                "time": r.time_nome,
                "pontos": r.pontos
            }
            for r in ranking
        ]
    }

    set_cache(slug, dados)
    return dados
>>>>>>> 8be9301d920511562386ab92c60d405addd85f91
@app.get("/liga/{slug}")
def liga_teste(slug: str):
    return {
        "status": "endpoint OK",
        "slug_recebido": slug
    }
