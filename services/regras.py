# Logica principal do negeocio (CRUD)
novas_tarefas = []

def menu_opcoes():
  print("------ BEM VINDO AO MENU DE TAREFAS ------")
  print("1 - Adicionar tarefas")
  print("2 - Visualizar a tarefas")
  print("3 - Atualizar tarefas")
  print("4 - Excluir tarefas")
  print("5 - Sair do menu de tarefas")

def adicionar_tarefas(): # CREATE  
  tarefa = input("Digite a tarefa: ")
  novas_tarefas.append(tarefa)
  
def visualizar_tarefa(): # READ
  
  for tarefa in novas_tarefas:
    print(tarefa)


def atualizar_tarefa(): # UPTDATE

  print("\nTarefas atuais:")

  for i, tarefa in enumerate(novas_tarefas):
    print(f"{i}. {tarefa}")
      
  indice = int(input("Digite o numero da tarefa para atualizar: "))  
  
  # Verifica se o indicde existe na lista
  if 0 <= indice < len(novas_tarefas):
    novo_texto = input("Digite a nova tarefa: ")
    
    # Atualizar a tarefa
    novas_tarefas[indice] = novo_texto
  else:
    print("Indice invalido!")
    


def deletar_tarefa(): # DELETE
  print("\nTarefas atuais:")

  for i, tarefa in enumerate(novas_tarefas):
    print(f"{i}  {tarefa}")
    
  indice_deletar = int(input("Digite o numero da tarefa para deletar: "))
    
    # Validação de indice
  if 0 <= indice_deletar < len(novas_tarefas):
    
    # Deletar tarefa
      novas_tarefas.pop(indice_deletar)
      print("Tarefa removida com sucesso!")
  else:
      print("Indice invalido!")

  print(f"Lista atualizada: {novas_tarefas}")