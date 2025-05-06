from pydantic import BaseModel
from typing import Optional
from datetime import date

class Adocao(BaseModel):
    id: Optional[int]
    pet_id: int
    tutor_id: int
    adotante_id: int
    data_adocao: date
