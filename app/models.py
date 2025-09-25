from pydantic import BaseModel, Field
from typing import Optional, Literal

TipoMovimiento = Literal["ingreso", "egreso"]

class MovimientoIn(BaseModel):
    tipo: TipoMovimiento
    monto: float = Field(..., ge=0)
    categoria: Optional[str] = None
    descripcion: Optional[str] = None

class Movimiento(MovimientoIn):
    id: int
