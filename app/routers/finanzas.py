from fastapi import APIRouter, HTTPException, status
from typing import List
from ..db import db
from ..models import Movimiento, MovimientoIn

router = APIRouter(prefix="/finanzas", tags=["finanzas"])

@router.get("/movimientos", response_model=List[Movimiento])
def listar_movimientos():
    return db.listar()

@router.post("/movimientos", response_model=Movimiento, status_code=status.HTTP_201_CREATED)
def crear_movimiento(payload: MovimientoIn):
    return db.crear(payload)

@router.get("/movimientos/{mov_id}", response_model=Movimiento)
def obtener_movimiento(mov_id: int):
    mov = db.obtener(mov_id)
    if not mov:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return mov

@router.get("/resumen")
def resumen_financiero():
    return db.resumen()
