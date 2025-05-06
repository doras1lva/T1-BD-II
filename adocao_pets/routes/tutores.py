from fastapi import APIRouter
from models.tutor import Tutor
from database import db

router = APIRouter()
collection = db["adocoes_pets"]

@router.post("/")
def criar_tutor(tutor: Tutor):
    tutor_dict = tutor.dict(exclude_unset=True)
    result = collection.insert_one(tutor_dict)
    return {"id": str(result.inserted_id)}

@router.get("/")
def listar_tutores():
    tutores = list(collection.find())
    for t in tutores:
        t["id"] = str(t["_id"])
        del t["_id"]
    return tutores
