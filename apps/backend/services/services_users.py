from apps.backend.models.usuario import Usuario
from apps.backend.schemas.Schema import usuarioSchema,UsuarioLogin , UsuarioAtualizar
from apps.backend.utils.utils import transforma_senha_hash,verificar_senha,gerar_token
from apps.backend.repository.User_Repository import User_Repository

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
      raise ValueError("E-mail ou Senha invalidos ")

    # verifica se a senha é a mesma
    senha_user = verificar_senha(body_usuario.senha, usuario_existe["senha_hash"])
    
    # senha invalida 
    if not senha_user:
      raise ValueError("E-mail ou Senha invalidos ")
   
  
    # gera JWT
    token =  gerar_token(usuario_existe["id_usuario"])
    
    return token
  
  def service_delete_user(self, id):
    ...
    
gerenciador_user = Gerenciador_User_Service()



