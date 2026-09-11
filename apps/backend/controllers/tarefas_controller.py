from apps.backend.schemas.Schema import tarefaSchema
from apps.backend.services.services_tarefa import gerenciador_Tarefas_Service

def controller_criar_tarefa(body_tarefa: tarefaSchema,id_user):
  return  gerenciador_Tarefas_Service.adicionar_tarefas(body_tarefa,id_user)

def controller_listar_tarefa(id):
  return gerenciador_Tarefas_Service.visualizar_tarefa(id)

def controller_atualizar_tarefa_id(id,body_tarefa:tarefaSchema, id_user):
  return gerenciador_Tarefas_Service.atualizar_tarefa(id,body_tarefa, id_user)

def controller_deletar_tarefa(id,id_user):
  return gerenciador_Tarefas_Service.deletar_tarefa(id,id_user)