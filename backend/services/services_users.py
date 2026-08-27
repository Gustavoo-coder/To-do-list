from backend.models.usuario import Usuario
from backend.schemas.Schema import usuarioSchema,UsuarioLogin , UsuarioAtualizar
from backend.utils.hash import transforma_senha_hash,verificar_senha
from backend.repository.User_Repository import User_Repository

class Gerenciador_User_Service():
  def __init__(self) -> None:
    self.banco_user = User_Repository() #injeção de depêndencia
    
  def service_criar_user(self,body_user:usuarioSchema):
     
      senha_has = transforma_senha_hash(body_user.senha)
     
     # recebe o modelo de dados vindo da API e adapta para classe existente do sistema 
      user = Usuario(body_user.nome_usuario, body_user.email, senha_has)
      
      
      resultado_user = self.banco_user.criar_usuario(user)
      
      return resultado_user
    
   
  def service_alterar_user(self, body_usuario: UsuarioAtualizar, id):
    novos_dados_user = body_usuario.model_dump(exclude_unset=True) # Pega só o que foi enviado
    
    #passa pro banco
    resultado_user = self.banco_user.atualizar_usuario(novos_dados_user,id)
    
        
    return resultado_user    

  def service_autenticar_user(self,body_usuario:UsuarioLogin ):
    
    # busca pelo banco o email enviado do login
    usuario_existe = self.banco_user.verificar_usuario_email(body_usuario.email)
    
    # usuario não existe
    if not usuario_existe:
      raise ValueError("Email ou Senha invalidos ")

    # #  verifica senha
    # senha_valida = verificar_senha(body_usuario.senha, usuario_existe["senha_hash"])
    
    # #  senha invalida
    # if not senha_valida:
    #   raise ValueError("Email ou Senha invalidos ")
        
    return usuario_existe
  
  def service_delete_user(self, id):
    ...
    
gerenciador_user = Gerenciador_User_Service()



