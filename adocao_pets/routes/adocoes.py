from fastapi import APIRouter
from models.adocao import Adocao
from database import db

router = APIRouter()
collection = db["adocoes_pets"]

@router.post("/")
def registrar_adocao(adocao: Adocao):
    adocao_dict = adocao.dict(exclude_unset=True)
    result = collection.insert_one(adocao_dict)
    return {"id": str(result.inserted_id)}

@router.get("/")
def listar_adocoes():
    adocoes = list(collection.find())
    for a in adocoes:
        a["id"] = str(a["_id"])
        del a["_id"]
    return adocoes
