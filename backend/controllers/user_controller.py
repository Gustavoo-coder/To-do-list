from backend.schemas.Schema import usuarioSchema
from backend.services.services_users import gerenciador_user

def criar_user(body_user:usuarioSchema):
  return  gerenciador_user.service_criar_user(body_user)