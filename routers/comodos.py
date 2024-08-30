from fastapi import APIRouter
from schemas.comodos import ComodoCreate, ComodoRead, ComodoUpdate
from models.comodos import ComodoDB

router = APIRouter(prefix="/comodos", tags=["CÔMODOS"])

@router.post("/")
def criar_comodo(novo_comodo: ComodoCreate):
    comodo = ComodoDB.create(**novo_comodo.model_dump())
    return novo_comodo

@router.get(path="/", response_model=list[ComodoRead])
def listar_comodos():
    comodos = ComodoDB.select()
    return comodos

@router.get(path="/{id}", response_model=ComodoRead)
def listar_comodo(id):
    comodo = ComodoDB.get_or_none(ComodoDB.id == id)
    return comodo

@router.put("/{id}", response_model=ComodoRead)
def atualizar_comodo(id, comodo_atualizado: ComodoUpdate):
    comodo = ComodoDB.get(ComodoDB.id == id)
    comodo.nome = comodo_atualizado.nome
    comodo.save()
    return comodo

@router.delete("/{id}")
def eliminar_comodo(id):
    comodo = ComodoDB.get(ComodoDB.id == id)
    comodo.delete_instance()
    return comodo
