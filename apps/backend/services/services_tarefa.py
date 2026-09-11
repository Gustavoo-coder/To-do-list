from apps.backend.models.tarefa import Tarefa
from apps.backend.repository.Tarefa_Repository import Repository_banco
from apps.backend.schemas.Schema import tarefaSchema


class GerenciadorTarefas_Service():
  def __init__(self):
    self.repo_banco = Repository_banco() #Injeção de Dependência
    
  def adicionar_tarefas(self,dados_tarefa: tarefaSchema,id_user):
    
        print(f"SERVICE{id_user}")
        # recebe o modelo de dados vindo da API e adapta para classe existente do sistema 
        tarefa = Tarefa(dados_tarefa.nome_tarefa,dados_tarefa.descricao_tarefa, dados_tarefa.status_tarefa,id_user)
        
        resultado = self.repo_banco.salvar_tarefa(tarefa) # chama o banco

        return resultado
    
  
  
  def visualizar_tarefa(self,id):
    
    tarefas = self.repo_banco.listar_tarefas(id)
    return tarefas 
  
  
  def atualizar_tarefa(self,id, nova_tarefa:tarefaSchema, id_user):
        
          # Verifca se a tarefa existe
          tarefa_exis= self.repo_banco.listar_tarefa_id(id)

          print(tarefa_exis)
          
          if not tarefa_exis: # verifca se existe a tarefa
           raise ValueError("Tarefa não encontrada!")
          
          if tarefa_exis["id_usuario"] != id_user :
            raise ValueError("Você só pode atualizar tarefas criadas por você")
          
          else:
            resultado = self.repo_banco.update_tarefa_id(id, nova_tarefa)
          
          return resultado
            
  
  def deletar_tarefa(self,id, id_user): 

        # verifica se a tarefa existe
        tarefa_existe = self.repo_banco.listar_tarefa_id(id)
      
        
        if not tarefa_existe:
          raise ValueError("Tarefa não encontrada ou já excluida")
        
        elif id_user != tarefa_existe["id_usuario"]:
          raise ValueError("Você só pode deletar tarefas criadas por você")
        
        else:        
          # passa pro banco
          resultado = self.repo_banco.deletar_tarefa_id(id)

        return resultado
        


gerenciador_Tarefas_Service = GerenciadorTarefas_Service()