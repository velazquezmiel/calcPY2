from pydantic import BaseModel, Field

class DispositivoCreate(BaseModel):
    residencia_id: int
    comodo_id: int
    nome: str
    potencia: int = Field(default=..., gt=0)
    uso_diario: float = Field(default=..., ge=0, le=24)

class DispositivoRead(BaseModel):
    residencia_id: int
    comodo_id: int
    nome: str
    potencia: int = Field(default=..., gt=0)
    uso_diario: float = Field(default=..., ge=0, le=24)

class DispositivoUpdate(BaseModel):
    nome: str
    potencia: int = Field(default=..., gt=0)
    uso_diario: float = Field(default=..., ge=0, le=24)