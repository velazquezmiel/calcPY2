from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException


from models.dependencia import DependenciaDB, UnidadeConsumidoraDB
from schemas.dependencia import (
    DependenciaCreate,
    DependenciaReadList,
    DependenciaReadOne,
    DependenciaUpdate,
)

router = APIRouter(prefix='/dependencias', tags=['DEPENDÊNCIAS'])


@router.post(path='', response_model=DependenciaReadOne)
def criar_dependencia(novo_dependencia: DependenciaCreate):
    dependencia = DependenciaDB.create(**novo_dependencia.model_dump())
    return dependencia


@router.get(path='', response_model=DependenciaReadList)
def listar_dependencias():
    dependencias = DependenciaDB.select()
    return {'dependencias': dependencias}

@router.get(
    path='/unidade-consumidora/{unidade_consumidora_id}',
    response_model=DependenciaReadList,
)
def listar_dependencia_da_unidade_de_consumo(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(
        UnidadeConsumidoraDB.id == unidade_consumidora_id
    )
    dependencias = DependenciaDB.select().where(
        DependenciaDB.unidade_consumidora == unidade_consumidora
    )
    # dependencias = DependenciaDB.select()
    return {'dependencias': dependencias}


@router.get(path='/{dependencia_id}', response_model=DependenciaReadOne)
def listar_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)

    if not dependencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Dependencias não encontrada.',
        )

    return dependencia


@router.patch(path='/{dependencia_id}', response_model=DependenciaReadOne)
def atualizar_dependencia(
    dependencia_id: int, novo_dependencia: DependenciaUpdate
):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    dependencia.nome = novo_dependencia.nome
    dependencia.save()
    return dependencia


@router.delete(path='/{dependencia_id}', response_model=DependenciaReadOne)
def excluir_dependenicas(dependencia_id: int):
    residencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    residencia.delete_instance()
    return residencia