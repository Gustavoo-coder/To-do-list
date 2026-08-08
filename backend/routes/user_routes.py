from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from backend.schemas.Schema import usuarioSchema
from backend.controllers.user_controller import criar_user

router_user = APIRouter(
  tags=["Rotas Usuario"]
)

@router_user.post("/usuarios")
def cadastrar_usuario(body_usuario:usuarioSchema): 
  try :
    
    usuario = criar_user(body_usuario)
    
    return JSONResponse(status_code=201, content={
      "Mensagem" : "Usuaria Criado com sucesso!"})
    
  except Exception as erro: 
    raise HTTPException(status_code=400, detail= str(erro))