from fastapi import FastAPI
import json
import os

app = FastAPI()

JSON_PATH = "dados_liga.json"

@app.get("/")
def root():
    return {"status": "API ONLINE"}

@app.get("/liga")
def liga():
    if not os.path.exists(JSON_PATH):
        return {"erro": "Arquivo JSON não encontrado"}
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
