from pydantic import BaseModel, EmailStr
from typing import Optional

class Tutor(BaseModel):
    id: Optional[int]
    nome: str
    email: EmailStr
    telefone: str
