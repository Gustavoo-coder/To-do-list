from pydantic import BaseModel,EmailStr

class tarefaSchema(BaseModel):
  nome_tarefa : str
  descricao_tarefa : str
  status_tarefa : str


class usuarioSchema(BaseModel):
  nome_usuario : str
  email : EmailStr
  senha: str
  
class UsuarioAtualizar(BaseModel):
  nome : str | None = None
  email : EmailStr | None = None
  senha_hash: str | None = None
  
  
class UsuarioLogin(BaseModel):
  email: EmailStr
  senha : str