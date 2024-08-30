from fastapi import APIRouter
from schemas.residencias import ResidenciaCreate, ResidenciaRead, ResidenciaUpdate
from models.residencias import ResidenciaDB

router = APIRouter(prefix="/residencias", tags=["RESIDÊNCIAS"])
@router.post("/")
def criar_residencia(nova_residencia: ResidenciaCreate):
    residencia = ResidenciaDB.create(**nova_residencia.model_dump())
    return nova_residencia

@router.get(path="/", response_model=list[ResidenciaRead])
def listar_residencias():
    residencias = ResidenciaDB.select()
    return residencias

@router.get(path="/{id}", response_model=ResidenciaRead)
def listar_residencia(id):
    residencia = ResidenciaDB.get_or_none(ResidenciaDB.id == id)
    return residencia

@router.put("/{id}", response_model=ResidenciaRead)
def atualizar_residencia(id, residencia_atualizada: ResidenciaUpdate):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.proprietario = residencia_atualizada.proprietario
    residencia.save()
    return residencia

@router.delete("/{id}")
def eliminar_residencia(id):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.delete_instance()
    return residencia