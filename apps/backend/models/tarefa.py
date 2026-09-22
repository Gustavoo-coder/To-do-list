class Tarefa():
    
  def __init__(self,nome_tarefa,descricao_tarefa,status_tarefa,id_usuario=None):
    self.id_usuario = id_usuario
    self.nome_tarefa = nome_tarefa
    self.descricao_tarefa = descricao_tarefa
    self.status_tarefa = status_tarefa


