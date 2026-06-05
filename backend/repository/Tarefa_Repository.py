from database.conexão_banco import conecta_banco
from services.tarefa import Tarefa
from sqlalchemy import text

class Repository_banco():
  
  # construtor recebe a conexão externamente 
  def __init__(self):
    self.engine = conecta_banco()
    
  
  # Metodos CRUD
  
  def salvar_tarefa(self,tarefa : Tarefa) -> None:
    
    try:
      # 1° abre a conexão com o banco
      with self.engine.connect() as conn:
        
        #2°escreve a query
        query = text("""
                    INSERT INTO tarefa (nome_tarefa, descricao_tarefa, status_tarefa)
                    VALUES(:nome_tarefa, :descricao_tarefa, :status_tarefa)
                    """)
        
        # 3° acessa os valores da classe tarefa segundo pesquisas (GOOGLE)
        conn.execute(query, {
          "nome_tarefa" : tarefa.nome_tarefa,
          "descricao_tarefa" : tarefa.descricao,
          "status_tarefa" : tarefa.status
        })

        # 4° envia pro banco
        conn.commit()
    
    
    except Exception as e:
      ValueError(f"Erro ao adiconar tarefa {e}")
    
  
  def listar_tarefas(self):
    
    try:
        
      # 1° abre a conexão com o banco
       with self.engine.connect() as conn:
        
        # 2° escreve a query 
        query_listar = text("""SELECT * FROM tarefa""")
        
        # 3° executa a query para encontar todos os resultados juntamente com fetchall
        resultado_query = conn.execute(query_listar).fetchall()
        
        # 4° Cria uma lista vazia para armazenar todas as tarefas
        tarefas_query = []
        
        # 5° Itera sobre cada resultado vindo da tupla
        # 6° Transforma cada indidce da tupla em um objeto da classe tarefa
        # 7° Adiciona o resultado final na lista tarefas_query
        # 8° Retorna o resultao
        for tarefa in resultado_query:
          tarefa = Tarefa(tarefa[1],tarefa[3],tarefa[2])
          tarefas_query.append(tarefa)
        
  
        return tarefas_query
    
    except Exception as e:
      ValueError(f"Erro ao ler tarefa {e}")