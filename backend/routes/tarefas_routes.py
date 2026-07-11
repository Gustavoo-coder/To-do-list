from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.schemas.tarefaSchema import tarefaSchema
from backend.controllers.tarefas_controller import criar_tarefa, listar_tarefa

# definindo prefixo nas rotas
router_tarefas = APIRouter(
  prefix="/tarefa",
  tags=["Rota Tarefas"]
)

@router_tarefas.post("/criarTarefa")
def criarTarefa(body_tarefa: tarefaSchema): # chama o endpoint
   tarefa_criada= criar_tarefa(body_tarefa) # chama  controller
   
  #  Resposta da rota
   return JSONResponse(status_code= 201, content={
    "Mensagem" : "Tarefa adiconada com Sucesso!",
    "Tarefa": tarefa_criada  
   })



@router_tarefas.get("/listarTarefas")
def listar_tarefas():
  lista_tarefa =  listar_tarefa()
  
  return JSONResponse(status_code=200, content={
    "Mensagem" : "Tarefas listadas com Sucesso!",
    "Tarefas" : lista_tarefa
  })
  
  
  
@router_tarefas.put("/atualizarTarefa")
def atualizar_tarefa():
  ...
  

@router_tarefas.delete("/deletarTarefa")
def deletar_tarefa():
 ...