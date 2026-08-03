from backend.schemas.tarefaSchema import tarefaSchema
from backend.services.services_tarefa import gerenciador_Tarefas_Service

def controller_criar_tarefa(body_tarefa: tarefaSchema):
  return  gerenciador_Tarefas_Service.adicionar_tarefas(body_tarefa)

def controller_listar_tarefa():
  return gerenciador_Tarefas_Service.visualizar_tarefa()

def controller_atualizar_tarefa_id(id,body_tarefa:tarefaSchema):
  return gerenciador_Tarefas_Service.atualizar_tarefa(id,body_tarefa)

def controller_deletar_tarefa(id):
  return gerenciador_Tarefas_Service.deletar_tarefa(id)