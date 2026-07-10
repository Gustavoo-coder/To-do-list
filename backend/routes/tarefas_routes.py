from fastapi import APIRouter
from backend.controller import tarefas_controller

# defindo prefixo nas rotas
router_tarefas = APIRouter(
  prefix="/tarefa",
  tags=["Rota Tarefas"]
)

@router_tarefas.post("/criarTarefa")
async def criar_tarefa():
 ...

@router_tarefas.get("/listarTarefas")
async def listar_tarefas():
 ...
  
@router_tarefas.put("/atualizarTarefa")
async def atualizar_tarefa():
  ...
  

@router_tarefas.delete("/deletarTarefa")
async def deletar_tarefa():
 ...