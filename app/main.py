from fastapi import FastAPI
from .routers import finanzas

app = FastAPI(title="API Tarea 3 – Finanzas")

# Registrar router de finanzas
app.include_router(finanzas.router)




