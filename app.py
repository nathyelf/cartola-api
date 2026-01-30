from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API Cartola no Render ONLINE"}

@app.get("/test")
def test():
    return {"msg": "Funcionando"}
