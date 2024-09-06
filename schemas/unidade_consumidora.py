from pydantic import BaseModel
from typing import List
from schemas.dependencia import DependenciaReadMany

class UnidadeConsumidoraCreate(BaseModel):
    nome: str
    tipo_id: int

class UnidadeConsumidoraUpdate(BaseModel):
    nome: str

class UnidadeConsumidoraRead(BaseModel):
    id: int
    nome: str
    tipo_id: int
    dependencias: List[DependenciaReadMany]

    class Config:
        orm_mode = True  # Adicione esta linha

class UnidadeConsumidoraReadForList(BaseModel):
    id: int
    nome: str
    tipo_id: int

    class Config:
        orm_mode = True  # Adicione esta linha

class UnidadeConsumidoraReadList(BaseModel):
    unidades_consumidoras: List[UnidadeConsumidoraReadForList]
