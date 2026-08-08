from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from backend.schemas.Schema import tarefaSchema

from backend.controllers.tarefas_controller import (
controller_criar_tarefa,
controller_listar_tarefa, 
controller_atualizar_tarefa_id,
controller_deletar_tarefa
)

# instanciando API ROUTER
router_tarefas = APIRouter(
  tags=["Rota Tarefas"]
)

@router_tarefas.post("/tarefas")
def criar_tarefas(body_tarefa: tarefaSchema): # chama o endpoint
  try:
    tarefa_criada= controller_criar_tarefa(body_tarefa) # chama  controller

      #  Resposta da rota
    return JSONResponse(status_code= 201, content={
        "Mensagem" : "Tarefa adiconada com Sucesso!",
        "Tarefa": tarefa_criada  
          })
 
  except Exception as error:
      raise HTTPException(status_code=400,detail= str(error))


@router_tarefas.get("/tarefas")
def listar_tarefas():
  lista_tarefa =  controller_listar_tarefa()
  
  return JSONResponse(status_code=200, content={
    "Mensagem" : "Tarefas listadas com Sucesso!",
    "Tarefas" : lista_tarefa
  })
  
  
  
@router_tarefas.put("/tarefas/{id}")
def atualizar_tarefas(id,body_tarefa:tarefaSchema):
  try:
    nova_tarefaController = controller_atualizar_tarefa_id(id,body_tarefa)
    return JSONResponse(status_code=200, content={
      "Mensagem" : "Tarefa atualizada com sucesso!",
      "Tarefa" : nova_tarefaController
    })
  except Exception as erro_id:
    raise HTTPException(status_code=404,detail=str(erro_id))

  

@router_tarefas.delete("/tarefas/{id}")
def deletar_tarefas(id):
  try:
      controller_deletar_tarefa(id)

      return JSONResponse(status_code=200, content={
        "Mensagem" : "Tarefa deletada com sucesso"})
  except Exception as erro:
    raise HTTPException(status_code= 404,detail=str(erro))