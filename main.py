from fastapi import FastAPI
from corpo_requisicao.routers import router
from valida_texto.router import router as valida
from valida_numeros.routers import router as valida_numero

app = FastAPI()

app.include_router(router)
app.include_router(valida)
app.include_router(valida_numero)
