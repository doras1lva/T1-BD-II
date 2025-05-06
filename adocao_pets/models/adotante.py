from pydantic import BaseModel
from typing import Optional

class Adotante(BaseModel):
    id: Optional[int]
    nome: str
    telefone: str
    endereco: str
