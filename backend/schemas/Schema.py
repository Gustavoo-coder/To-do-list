from pydantic import BaseModel,EmailStr

class tarefaSchema(BaseModel):
  nome_tarefa : str
  descricao_tarefa : str
  status_tarefa : str


class usuarioSchema(BaseModel):
  nome_usuario : str
  email : EmailStr
  senha: str
  
  