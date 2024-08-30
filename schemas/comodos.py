from pydantic import BaseModel, Field
from schemas.dispositivos import DispositivoRead
class ComodoCreate(BaseModel):
    nome: str
    residencia_id: int

class ComodoRead(BaseModel):
    nome: str
    residencia_id: int


class ComodoUpdate(BaseModel):
    nome: str
    residencia_id: int
    eletrodomesticos: list[DispositivoRead] = []

# teste