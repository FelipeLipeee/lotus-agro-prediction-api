from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dados(BaseModel):
    temperatura: float
    umidade: float

@app.get("/")
def home():
    return {"status": "online"}

@app.post("/predict")
def predict(dados: Dados):
    if dados.temperatura > 30 and dados.umidade < 40:
        risco = "Alto risco de seca - ligar irrigacao"
    elif dados.umidade > 80:
        risco = "Risco de fungos - umidade alta"
    else:
        risco = "Condicoes normais"

    return {
        "temperatura": dados.temperatura,
        "umidade": dados.umidade,
        "previsao": risco
    }

@app.get("/predict")
def predict_get(temperatura: float, umidade: float):
    if temperatura > 30 and umidade < 40:
        risco = "Alto risco de seca - ligar irrigacao"
    elif umidade > 80:
        risco = "Risco de fungos - umidade alta"
    else:
        risco = "Condicoes normais"

    return {
        "temperatura": temperatura,
        "umidade": umidade,
        "previsao": risco
    }
