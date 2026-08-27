from backend.schemas.Schema import usuarioSchema , UsuarioAtualizar, UsuarioLogin
from backend.services.services_users import gerenciador_user

def criar_user(body_usuario:usuarioSchema):
  return  gerenciador_user.service_criar_user(body_usuario)

def alterar_dados_user(body_usuario : UsuarioAtualizar,id):
  return gerenciador_user.service_alterar_user(body_usuario,id)

def user_login(body_usuario: UsuarioLogin):
  return gerenciador_user.service_autenticar_user(body_usuario)

def deletar_user(id):
  return gerenciador_user.service_delete_user(id)