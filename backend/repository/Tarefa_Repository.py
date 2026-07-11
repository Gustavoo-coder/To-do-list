from backend.database.conexão_banco import conecta_banco
from backend.models.tarefa import Tarefa
from sqlalchemy import text

class Repository_banco():
  
  # construtor recebe a conexão externamente 
  def __init__(self):
    self.engine = conecta_banco()
  
  def salvar_tarefa(self,tarefa : Tarefa):
    
    try:
      # 1° abre a conexão com o banco
      with self.engine.connect() as conn: # type: ignore
        
        #2°escreve a query
        query = text("""
                    INSERT INTO tarefa (nome_tarefa, descricao_tarefa, status_tarefa)
                    VALUES(:nome_tarefa, :descricao_tarefa, :status_tarefa)
                    RETURNING id_tarefa, nome_tarefa, descricao_tarefa, status_tarefa""")
        
        # 3° acessa os valores da classe tarefa
        resultado = conn.execute(query, {
          "nome_tarefa" : tarefa.nome_tarefa,
          "descricao_tarefa" : tarefa.descricao,
          "status_tarefa" : tarefa.status
        })
        
        # captura a tarefa do usuario criada
        tarefa_criada = resultado.fetchone()
        
        # 4° envia pro banco
        conn.commit()

        return dict(tarefa_criada._mapping) # type: ignore
      
    
    except Exception as e:
      raise ValueError(f"Erro ao adiconar tarefa {e}")
    
  
  def listar_tarefas(self):
    
    try:
        
      # 1° abre a conexão com o banco
       with self.engine.connect() as conn: # type: ignore
        
        # 2° escreve a query 
        query_listar = text("""SELECT * FROM tarefa""")
        
        # 3° executa a query para encontar todos os resultados juntamente com fetchall
        resultado_query = conn.execute(query_listar).fetchall()
        
        # 4° Cria uma lista vazia para armazenar todas as tarefas
        tarefas_query = []
        
        # Itera sobre cada resultado vindo da tupla
        for row in resultado_query:
          tarefas_query.append(dict(row._mapping)) # type: ignore
       
        return tarefas_query 
      
    except Exception as error:
      raise ValueError(f"Erro ao ler tarefa: {error}")
  
  
  def update_tarefa_id(self,tarefa:Tarefa,id):
    
    try :
      with self.engine.connect() as conn: # type: ignore
      
      # atualizar a tarefa 
        query_atualizar = text("""UPDATE tarefa SET nome_tarefa = :nome_tarefa, descricao_tarefa = :descricao_tarefa, status_tarefa = :status_tarefa WHERE id_tarefa = :id_tarefa""")
      
        conn.execute(query_atualizar,{
            "id_tarefa" : id,
            "nome_tarefa" : tarefa.nome_tarefa,
            "descricao_tarefa" : tarefa.descricao,
            "status_tarefa" : tarefa.status
          })

        # envia alterações pro banco
        conn.commit()
        
        
    except Exception as error:
      raise ValueError(f"Erro ao atualizar tarefa: {error}")
    
  def deletar_tarefa_id(self,id):
    try:
      # abre conexão com o banco
      with self.engine.connect() as conn:  # type: ignore
    
        # escrevo a query:
        query_deletar = text(""" DELETE FROM tarefa WHERE id_tarefa = :id_tarefa """)
        
        # passo os objetos da classe e execeto a query
        conn.execute(query_deletar,{
          "id_tarefa" : id
        })
      
        # envia alterações pro banco
        conn.commit()
        
    except Exception as error:
      raise ValueError(f"Erro ao excluir tarefa tarefa: {error}")
    
    
    