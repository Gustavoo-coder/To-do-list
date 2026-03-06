class Tarefa():
    
  def __init__(self,id,tarefa,descricao,status):
    self.id = id
    self.nome_tarefa = tarefa
    self.descricao = descricao
    self.status = status

# Verifica se não possui numeros digitados no input
    if tarefa.isdigit():
        raise ValueError("A tarefa deve conter apenas letras")
    elif len(tarefa) < 5:
      raise ValueError("Deve ter pelo 5 caracteres !")
    
  def __str__(self):
      return f"[{self.id}]  {self.nome_tarefa} | Descrição: {self.descricao} | Status: {self.status}"

