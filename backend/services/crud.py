# Logica principal do negeocio (CRUD)
from backend.services.tarefa import Tarefa

class Gerenciador_Tarefas():
  def __init__(self):
    self.novas_tarefas = []
    self.id_tarefa = 1
    
  def menu_opcoes(self):
    print("------ BEM VINDO AO MENU DE TAREFAS ------")
    print("1 - Adicionar tarefas")
    print("2 - Visualizar a tarefas")
    print("3 - Atualizar tarefas")
    print("4 - Excluir tarefas")
    print("5 - Sair do menu de tarefas")

  def adicionar_tarefas(self): # CREATE  
    
    while True:
      nome_tarefa = input("Digite a nova tarefa: ").strip()
      descricao_tarefa = input("Descrição da tarefa: ").strip()
      status_tarefa = input("Status da tarefa: ").strip()
      
      if not self.novas_tarefas:
        print("Nenhuma tarefa cadastrada")
      else:
        tarefa = Tarefa(self.id_tarefa,nome_tarefa,descricao_tarefa,status_tarefa)
        print(f"Tarefa: {tarefa.nome_tarefa} -  adicionada com sucesso!")
        self.novas_tarefas.append(tarefa)
        self.id_tarefa += 1
        break

  def visualizar_tarefa(self): # READ
    
    for tarefa in self.novas_tarefas:
      print(tarefa)


  def atualizar_tarefa(self): # UPTDATE

    print("\nTarefas atuais:")

    for i, tarefa in enumerate(self.novas_tarefas):
      print(
        f"Tarefa: [{i}] - {tarefa.nome_tarefa} | Descrição: {tarefa.descricao} | Status: {tarefa.status}"
      )
        
    indice = int(input("Digite o numero da tarefa para atualizar: "))
    
    # Verifica se o indicde existe na lista
    if 0 <= indice < len(self.novas_tarefas):
      novo_texto = input("Digite a nova tarefa: ")
      nova_descricao = input("Digite a descrição da tarefa: ")
      novo_status = input("Digite o novo status da tarefa: ")
      
      # Atualiza a lista de atributos do objetos
      self.novas_tarefas[indice].nome_tarefa = novo_texto
      self.novas_tarefas[indice].descricao = nova_descricao
      self.novas_tarefas[indice].status = novo_status
      print("Tarefa Atualizada!")
    else:
      print("Indice invalido!")
      


  def deletar_tarefa(self): # DELETE
    print("\nTarefas atuais:")

    for i, tarefa in enumerate(self.novas_tarefas):
      print(f"Tarefa: {i}  {tarefa}")
      
    indice_deletar = int(input("Digite o numero da tarefa para deletar: "))
      
      # Validação de indice
    if 0 <= indice_deletar < len(self.novas_tarefas):
      
      # Deletar tarefa
        self.novas_tarefas.pop(indice_deletar)
        print("Tarefa removida com sucesso!")
    else:
        print("Indice invalido!")

    print(f"Lista atualizada: {tarefa}")

gerenciador_tarefas_crud = Gerenciador_Tarefas()