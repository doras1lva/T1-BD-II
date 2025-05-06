from pydantic import BaseModel
from typing import Optional

class Pet(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    tipo: str  # Ex: cachorro, gato
    raca: str
    vacinado: bool
    castrado: bool
