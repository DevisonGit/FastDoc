from fastapi import FastAPI
from corpo_requisicao.routers import router
from valida_texto.router import router as valida

app = FastAPI()

app.include_router(router)
app.include_router(valida)
