from fastapi import APIRouter
from schemas.dispositivos import DispositivoCreate, DispositivoRead, DispositivoUpdate
from models.dispositivos import DispositivoDB

router = APIRouter(prefix="/dispositivos", tags=["DISPOSITIVOS"])

@router.post("/")
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    dispositivo = DispositivoDB.create(**novo_dispositivo.model_dump())
    return novo_dispositivo

@router.get("/", response_model=list[DispositivoRead])
def listar_dispositivos():
    dispositivo = DispositivoDB.select()
    return dispositivo

@router.get("/{id}", response_model=DispositivoRead)
def listar_dispositivo(id):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == id)
    return dispositivo

@router.put("/{id}", response_model=DispositivoRead)
def atualizar_dispositivo(id, dispositivo_atualizado: DispositivoUpdate):
    dispositivo = DispositivoDB.get(DispositivoDB.id == id)
    dispositivo.nome = dispositivo_atualizado.nome
    dispositivo.potencia = dispositivo_atualizado.potencia
    dispositivo.uso_diario = dispositivo_atualizado.uso_diario
    dispositivo.save()
    return dispositivo

@router.delete("/{id}")
def eliminar_dispositivo(id):
    dispositivo = DispositivoDB.get(DispositivoDB.id == id)
    dispositivo.delete_instance()
    return dispositivo

