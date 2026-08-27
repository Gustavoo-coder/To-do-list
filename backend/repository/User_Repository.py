from backend.database.conexão_banco import conecta_banco
from sqlalchemy import text
from backend.schemas.Schema import UsuarioLogin
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
        raise ValueError (f"Erro ao inserir usuario {error}")
      
      
  def atualizar_usuario(self,usuario,id):
    try:
      colunas = []
      
      for chave in usuario.keys():  
          colunas.append(f"{chave} = :{chave}")

      set_campo = ", ".join(colunas)
      
      with self.engine.connect() as conn: # type: ignore
        
        query = text(f"""
                     UPDATE usuario SET {set_campo}
                     WHERE id_usuario = :id_usuario
                     RETURNING nome,email,senha_hash""")
        
        resultado = conn.execute(query,{
          "id_usuario" : id,
          **usuario
        })
        
        novos_dados = resultado.fetchone() 
        print(novos_dados)
        
        conn.commit()
        
        return dict(novos_dados._mapping) # type: ignore
      
    except Exception as error:
      raise ValueError(f"Erro ao atualizar dados do usuario {error}")
    
  def verificar_usuario_email(self,email):
    try:
      with self.engine.connect() as conn: #type: ignore
      
        query = text("""SELECT nome, email, senha_hash FROM usuario WHERE email = :email
                     """)
        
        user_email = conn.execute(query,{
          "email" : email}).scalar_one_or_none()
        
        
        
        return user_email #type: ignore 

    except Exception as error:
      raise ValueError(f" {error}")