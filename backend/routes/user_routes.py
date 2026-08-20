from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from backend.schemas.Schema import usuarioSchema
from backend.schemas.Schema import UsuarioAtualizar
from backend.controllers.user_controller import criar_user, alterar_dados_user, deletar_user

router_user = APIRouter(
  tags=["Rotas Usuario"]
)

@router_user.post("/usuarios")
def cadastrar_usuario(body_usuario:usuarioSchema): 
  try :
    
    criar_user(body_usuario)
    
    return JSONResponse(status_code=201, content={
      "Mensagem" : "Usuario criado com sucesso!"})
    
  except Exception as erro: 
    raise HTTPException(status_code=400, detail= str(erro))
  
  
# Login JWT 

# ----------------


@router_user.patch("/usuarios/{id}")
def alterar_dado(body_usuario : UsuarioAtualizar, id):
  try:
    dados_usuario = alterar_dados_user(body_usuario, id)
    
    return JSONResponse(status_code=200, content = 
    {"Mensagem" : "Dados alterados com sucesso" , 
    "Usuario"  : dados_usuario })
    
  except Exception as erro:
    raise HTTPException(status_code=400, detail= str(erro))
  
  
  
@router_user.delete("/usuarios{id}")
def deletar_usuario(id):
  try:
    deletar_user(id)
    
    return JSONResponse(status_code=200, content="Usuario deletado com sucesso")
  except Exception as error:
    return HTTPException(status_code=500, detail=str(error))