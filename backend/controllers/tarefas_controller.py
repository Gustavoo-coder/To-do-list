from backend.schemas.tarefaSchema import tarefaSchema
from backend.services.services_tarefa import gerenciador_tarefas_crud

def criar_tarefa(body_tarefa: tarefaSchema):
  return  gerenciador_tarefas_crud.adicionar_tarefas(body_tarefa)

def listar_tarefa():
  return gerenciador_tarefas_crud.visualizar_tarefa()

def atualizar_tarefa_id(id,body_tarefa:tarefaSchema):
  return gerenciador_tarefas_crud.atualizar_tarefa(id,body_tarefa)