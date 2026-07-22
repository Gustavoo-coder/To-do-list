from backend.models.tarefa import Tarefa
from backend.repository.Tarefa_Repository import Repository_banco
from backend.schemas.tarefaSchema import tarefaSchema

class GerenciadorTarefas():
  def __init__(self):
    self.repo_banco = Repository_banco() #Injeção de Dependência
    
  def adicionar_tarefas(self,dados_tarefa: tarefaSchema):
    try:
        # recebe o modelo de dados vindo da API e adapta para classe existente do sistema 
        tarefa = Tarefa(dados_tarefa.nome_tarefa,dados_tarefa.descricao_tarefa, dados_tarefa.status_tarefa)
        
        resultado = self.repo_banco.salvar_tarefa(tarefa) # chama o banco

        return resultado
    
    except Exception as error:
      print(f"Erro ao inserir tarefa", error)
  
  
  def visualizar_tarefa(self):
    
    tarefas = self.repo_banco.listar_tarefas()
    return tarefas 
  
  
  
  def atualizar_tarefa(self,id, nova_tarefa:Tarefa): # UPDATE
        
          # Verifca se a tarefa existe
          self.repo_banco.listar_tarefa_id(id)
          
          if self.repo_banco: # se existe a tarefa, passo pro repository
            return self.repo_banco.update_tarefa_id(nova_tarefa,id)
          
          else:
            raise ValueError("Tarefa não encontrada!")
          
            
  
  def deletar_tarefa(self): # DELETE
   
    print("\nTarefas atuais:")

    resultado_tarefas = self.repo_banco.listar_tarefas()
    
    for i, tarefa in enumerate(resultado_tarefas, start=1):
      print(f"Tarefa: {i}  {tarefa.nome_tarefa}")
    
    
    try:
      indice_deletar = int(input("Digite o numero da tarefa para deletar: "))
    except ValueError:
      print("Erro: Digite um numero valido")
      return
    
    # Validação de indice
    if 1 <= indice_deletar <= len(resultado_tarefas):
      
      # Deletar tarefa
        tarefa = resultado_tarefas[indice_deletar -1] # aqui
        self.repo_banco.deletar_tarefa_id(tarefa.id)
        print("Tarefa removida com sucesso!")
    else:
        print("Indice invalido!")


gerenciador_tarefas_crud = GerenciadorTarefas()