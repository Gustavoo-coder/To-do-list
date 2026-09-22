from pwdlib import PasswordHash
from jwt import encode, decode,DecodeError,ExpiredSignatureError
from datetime import datetime,timedelta,timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from apps.backend.repository.User_Repository import User_Repository
import os

expiracao_token = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","")
chave_secreta = os.getenv("SECRET_KEY","")
senha_hash = PasswordHash.recommended()

repo_user = User_Repository()

# extrai o token e tokeUrl mostra pro fastapi onde o token é obtido
decodificar_token = OAuth2PasswordBearer(tokenUrl="/login-usuarios")

def transforma_senha_hash(senha:str) -> str:
  return senha_hash.hash(senha)


def verificar_senha(senha_login: str,  senha_banco:str):
  return senha_hash.verify(senha_login,senha_banco)


def gerar_token(id_usuario : int):
  
  # calcula a hora atual e adiciona + 30 minutos
  expiracao = datetime.now(timezone.utc) + timedelta(minutes = float(expiracao_token))
  
  # a sub é o id do usuario
  info = {"sub": str(id_usuario), "exp": expiracao}
  
  # encodifica header e payload para assinatura
  token = encode(info, chave_secreta, algorithm=os.getenv("ALGORITHM"))
  
  return token


def validar_token(token: str = Depends(decodificar_token)):
  try:
    # decodifica o token 
    id_user = decode(token,chave_secreta,algorithms= os.getenv("ALGORITHM"))
     
    # busca o id enviado no token  
    id_payload = id_user.get("sub")
    
    # se nao tiver o id do usuario
    if not id_payload:
      raise HTTPException(status_code=401, detail="Token invalido")  
    
    # caso o usuario não exista no banco 
    user_existe = repo_user.buscar_user(id_payload)
    
    if not user_existe:
      raise  HTTPException(status_code=401, detail="Token invalido")
    
    return user_existe["id_usuario"]
  except  DecodeError:
    raise HTTPException(status_code=401, detail="Token invalido") 
  
  except ExpiredSignatureError :
    raise HTTPException(status_code=401, detail="Token expirado")