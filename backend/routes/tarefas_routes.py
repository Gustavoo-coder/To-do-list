from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from backend.schemas.tarefaSchema import tarefaSchema
from backend.controllers.tarefas_controller import criar_tarefa, listar_tarefa, atualizar_tarefa_id

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
  
  
  
@router_tarefas.put("/atualizarTarefa/{id_tarefa}")
def atualizar_tarefa(id_tarefa:int,body_tarefa:tarefaSchema):
  try:
    nova_tarefaController = atualizar_tarefa_id(id_tarefa,body_tarefa)
    return JSONResponse(status_code=200, content=[{
      "Mensagem" : "Tarefa atualizada com sucesso!",
      "Tarefa" : nova_tarefaController
    }])
  except Exception as error:
    raise HTTPException(status_code=400,detail=f"Erro ao atualizar tarefa: {error}" )
  

@router_tarefas.delete("/deletarTarefa")
def deletar_tarefa():
 ...