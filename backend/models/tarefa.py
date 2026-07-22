class Tarefa():
    
  def __init__(self,tarefa,descricao_tarefa,status_tarefa,id=None):
    self.id = id
    self.nome_tarefa = tarefa
    self.descricao_tarefa = descricao_tarefa
    self.status_tarefa = status_tarefa

# Verifica se não possui numeros digitados no input
    if tarefa.isdigit():
        raise ValueError("A tarefa deve conter apenas letras")

