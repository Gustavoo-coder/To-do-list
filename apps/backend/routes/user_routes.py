from fastapi import APIRouter , HTTPException, Depends
from fastapi.responses import JSONResponse
from apps.backend.schemas.Schema import usuarioSchema , UsuarioAtualizar , UsuarioLogin, Token
from apps.backend.controllers.user_controller import criar_user, alterar_dados_user, deletar_user,user_login
from apps.backend.utils.utils import validar_token

router_user = APIRouter(
  tags=["Rotas - usuario"]
)

@router_user.post("/usuarios")
def cadastrar_usuario(body_usuario:usuarioSchema): 
  try :
    
    criar_user(body_usuario)
    
    return JSONResponse(status_code=201, content={
      "Mensagem" : "Usuario criado com sucesso!"})
    
  except Exception as erro: 
    raise HTTPException(status_code=400, detail= str(erro))
  
  

@router_user.post("/login-usuarios", response_model=Token)
def login_user(body_usuario: UsuarioLogin):
  try:
    usuario = user_login(body_usuario)
    
    if not usuario: 
      return JSONResponse(status_code=401, content={"Mensagem" : "E-mail ou Senha invalidos"})
    
    return {"access_token" : usuario, "token_type": "Bearer"}

  except Exception as error:
    raise HTTPException(status_code=404, detail= str(error))



@router_user.patch("/usuarios")
def alterar_dado(body_usuario : UsuarioAtualizar , id_user: int = Depends(validar_token)):
  try:
    dados_usuario = alterar_dados_user(body_usuario, id_user)
    
    return JSONResponse(status_code=200, content = 
    {"Mensagem" : "Dados alterados com sucesso" , 
    "Usuario"  : dados_usuario })
    
  except Exception as erro:
    raise HTTPException(status_code=400, detail= str(erro))
  
  
  
@router_user.delete("/usuarios")
def deletar_usuario(id = Depends(validar_token)):
  try:
    deletar_user(id)
    
    return JSONResponse(status_code=200, content="Usuario deletado com sucesso")
  except Exception as error:
    return HTTPException(status_code=500, detail=str(error))