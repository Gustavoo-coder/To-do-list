from backend.database.conexão_banco import conecta_banco
from sqlalchemy import text
from backend.schemas.Schema import usuarioSchema
from backend.models.usuario import Usuario 

class User_Repository():
  def __init__(self) -> None:
    self.engine = conecta_banco()
    
  def criar_usuario(self,usuario:Usuario):
      try:
        
        # abre a conexão
          with self.engine.connect() as conn: # type: ignore
          
            # escreve a query
            query = text("""INSERT INTO usuario (nome, email, senha_hash) 
                       VALUES (:nome, :email, :senha_hash)
                       RETURNING id_usuario,nome,email,senha_hash""")
            
            resultado = conn.execute(query,{
              "nome" : usuario.nome_usuario,
              "email" : usuario.email,
              "senha_hash" : usuario.senha
            })
            
            user_criado = resultado.fetchone()
            
            # envia as alterações
            conn.commit()
            
            return dict(user_criado._mapping) # type: ignore
      except Exception as error:
        raise ValueError (f"Erro ao inserir usario {error}")