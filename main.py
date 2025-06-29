from fastapi import FastAPI
from corpo_requisicao.routers import router

app = FastAPI()

app.include_router(router)
