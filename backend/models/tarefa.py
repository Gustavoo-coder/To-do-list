class Tarefa():
    
  def __init__(self,tarefa,descricao,status,id=None):
    self.id = id
    self.nome_tarefa = tarefa
    self.descricao = descricao
    self.status = status

# Verifica se não possui numeros digitados no input
    if tarefa.isdigit():
        raise ValueError("A tarefa deve conter apenas letras")
  
  def __str__(self):
      return f" Tarefa: {self.nome_tarefa} | Descrição: {self.descricao} | Status: {self.status}"
