from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API ONLINE"}

@app.get("/liga/{slug}")
def liga(slug: str):
    return {
        "ok": True,
        "slug_recebido": slug
    }
