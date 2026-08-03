from backend.models.tarefa import Tarefa
from backend.repository.Tarefa_Repository import Repository_banco
from backend.schemas.tarefaSchema import tarefaSchema


class GerenciadorTarefas_Service():
  def __init__(self):
    self.repo_banco = Repository_banco() #Injeção de Dependência
    
  def adicionar_tarefas(self,dados_tarefa: tarefaSchema):
    
        # recebe o modelo de dados vindo da API e adapta para classe existente do sistema 
        tarefa = Tarefa(dados_tarefa.nome_tarefa,dados_tarefa.descricao_tarefa, dados_tarefa.status_tarefa)
        
        resultado = self.repo_banco.salvar_tarefa(tarefa) # chama o banco

        return resultado
    
  
  
  def visualizar_tarefa(self):
    
    tarefas = self.repo_banco.listar_tarefas()
    return tarefas 
  
  
  def atualizar_tarefa(self,id, nova_tarefa:tarefaSchema):
        
          # Verifca se a tarefa existe
          tarefa_exis= self.repo_banco.listar_tarefa_id(id)
        
          
          if not tarefa_exis: # verifca se existe a tarefa
           raise ValueError("Tarefa não encontrada!")
          
          else:
            resultado = self.repo_banco.update_tarefa_id(id, nova_tarefa)
          
          return resultado
            
  
  def deletar_tarefa(self,id): 

        # verifica se a tarefa existe
        tarefa_existe = self.repo_banco.listar_tarefa_id(id)
      
        
        if not tarefa_existe:
          raise ValueError("Tarefa não encontrada ou já excluida")
        
        else:        
          # passa pro banco
          resultado = self.repo_banco.deletar_tarefa_id(id)

        return resultado
        


gerenciador_Tarefas_Service = GerenciadorTarefas_Service()