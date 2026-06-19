from backend.models.tarefa import Tarefa
from backend.repository.Tarefa_Repository import Repository_banco
class GerenciadorTarefas():
  def __init__(self):
    self.repo_banco = Repository_banco() #Injeção de Dependência
    
  def menu_opcoes(self):
    print("------ BEM VINDO AO MENU DE TAREFAS ------")
    print("1 - Adicionar tarefas")
    print("2 - Visualizar a tarefas")
    print("3 - Atualizar tarefas")
    print("4 - Excluir tarefas")
    print("5 - Sair do menu de tarefas")

  def adicionar_tarefas(self):  
      nome_tarefa = input("Digite a nova tarefa: ").strip()
      descricao_tarefa = input("Descrição da tarefa: ").strip()
      status_tarefa = input("Status da tarefa: ").strip()
    
      tarefa = Tarefa(nome_tarefa,descricao_tarefa,status_tarefa)
      
      self.repo_banco.salvar_tarefa(tarefa)
      print(f"Tarefa: {tarefa.nome_tarefa} - adicionada com sucesso!")

      
      
  def visualizar_tarefa(self):
    tarefas = self.repo_banco.listar_tarefas()
    
    for tarefa in tarefas:
      print(tarefa)
  
  def atualizar_tarefa(self): # UPDATE
          
          tarefas = self.repo_banco.listar_tarefas()
          
          print("\nTarefas atuais:")
          
          for i, tarefa in enumerate(tarefas,start=1):
            print(
                f"Tarefa: [{i}] - {tarefa.nome_tarefa} | Descrição: {tarefa.descricao} | Status: {tarefa.status}"
            )  
          
          try:
            indice_tarefa = int(input("Digite o numero da tarefa para atualizar: "))
 
          except ValueError:
            print("Digite um identificador unico")
            return
          
          # Verifica se o indice_tarefa existe na lista
          if 0 <= indice_tarefa < len(tarefas):
                novo_texto = input("Digite a nova tarefa: ")
                nova_descricao = input("Digite a descrição da tarefa: ")
                novo_status = input("Digite o novo status da tarefa: ")
                
                # compactando obejetos soltos na class tarefa
                tarefa_nova = Tarefa(novo_texto,nova_descricao,novo_status)
                
                # atualiza a tarefa chamando repository
                self.repo_banco.update_tarefa_id(tarefa_nova,tarefas[indice_tarefa].id)
                print("Tarefa Atualizada!")
          else:
            print("Indice invalido!")
            
  
  def deletar_tarefa(self): # DELETE
   
    if not self.novas_tarefas:
      print("Nenhuma tarefa disponivel!")
      return
    
    print("\nTarefas atuais:")

    for i, tarefa in enumerate(self.novas_tarefas):
      print(f"Tarefa: {i}  {tarefa}")
      
    try:
      indice_deletar = int(input("Digite o numero da tarefa para deletar: "))
    except ValueError:
      print("Erro: Digite um numero valido")
      return
    
    # Validação de indice
    if 0 <= indice_deletar < len(self.novas_tarefas):
      
      # Deletar tarefa
        self.novas_tarefas.pop(indice_deletar)
        print("Tarefa removida com sucesso!")
    else:
        print("Indice invalido!")


gerenciador_tarefas_crud = GerenciadorTarefas()