from fastapi import FastAPI
app = FastAPI(title= "FastAPI - To do list")

from apps.backend.routes import tarefas_routes
from apps.backend.routes import user_routes

# renderizando as rotas
app.include_router(tarefas_routes.router_tarefas)
app.include_router(user_routes.router_user)

