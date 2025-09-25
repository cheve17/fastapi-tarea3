from typing import Dict, List
from .models import Movimiento, MovimientoIn

class InMemoryDB:
    def __init__(self):
        self._seq = 0
        self._data: Dict[int, Movimiento] = {}

    def listar(self) -> List[Movimiento]:
        return list(self._data.values())

    def crear(self, payload: MovimientoIn) -> Movimiento:
        self._seq += 1
        mov = Movimiento(id=self._seq, **payload.model_dump())
        self._data[mov.id] = mov
        return mov

    def obtener(self, mov_id: int) -> Movimiento | None:
        return self._data.get(mov_id)

    def resumen(self):
        ingresos = sum(m.monto for m in self._data.values() if m.tipo == "ingreso")
        egresos  = sum(m.monto for m in self._data.values() if m.tipo == "egreso")
        balance  = ingresos - egresos
        return {
            "ingresos": ingresos,
            "egresos": egresos,
            "balance": balance,
            "n_movimientos": len(self._data)
        }

db = InMemoryDB()
