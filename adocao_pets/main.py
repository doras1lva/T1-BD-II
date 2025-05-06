from fastapi import FastAPI
from routes import pets, tutores, adotantes, adocoes

app = FastAPI(title="Sistema de Adoção de Pets")

app.include_router(pets.router, prefix="/pets", tags=["Pets"])
app.include_router(tutores.router, prefix="/tutores", tags=["Tutores"])
app.include_router(adotantes.router, prefix="/adotantes", tags=["Adotantes"])
app.include_router(adocoes.router, prefix="/adocoes", tags=["Adoções"])
