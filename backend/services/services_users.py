from backend.models.usuario import Usuario
from backend.schemas.Schema import usuarioSchema
from backend.schemas.Schema import UsuarioAtualizar
from backend.utils.hash import transforma_senha_hash
from backend.repository.User_Repository import User_Repository

class Gerenciador_User_Service():
  def __init__(self) -> None:
    self.banco_user = User_Repository() #injeção de depêndencia
    
  def service_criar_user(self,body_user:usuarioSchema):
     
      senha_has = transforma_senha_hash(body_user.senha)
     
     # recebe o modelo de dados vindo da API e adapta para classe existente do sistema 
      user = Usuario(body_user.nome_usuario, body_user.email, senha_has)
      
      # passa pro banco
      resultado_user = self.banco_user.criar_usuario(user)
      
      return resultado_user
    
  
  def service_alterar_user(self, body_usuario: UsuarioAtualizar, id):
    novos_dados_user = body_usuario.model_dump(exclude_unset=True) # Pega só o que foi enviado
    
    #passa pro banco
    resultado_user = self.banco_user.atualizar_usuario(novos_dados_user,id)
    
    print(resultado_user)
        
    return resultado_user    

  
  
  def service_delete_user(self, id):
    ...
    
gerenciador_user = Gerenciador_User_Service()



