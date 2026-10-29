# Lotus Agro API (Atividade PaaS)

API em Python (FastAPI) para previsao de risco climatico agricola a partir de temperatura e umidade, configurada para deploy em PaaS (Render).

## Arquivos
- `main.py`: Codigo da API com a rota `/predict`.
- `requirements.txt`: Dependencias do Python.
- `Procfile`: Comando de inicializacao na nuvem.

## Como testar
- POST ou GET em `/predict?temperatura=28&umidade=80&cultura=Soja`
