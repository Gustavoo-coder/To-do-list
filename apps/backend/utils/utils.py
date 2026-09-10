from pwdlib import PasswordHash
import jwt
import os
from datetime import datetime,timedelta,timezone

expiracao_token = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",""))

chave_secreta = os.getenv("SECRET_KEY","")

senha_hash = PasswordHash.recommended()


def transforma_senha_hash(senha:str) -> str:
  return senha_hash.hash(senha)


def verificar_senha(senha_login: str,  senha_banco:str):
  return senha_hash.verify(senha_login,senha_banco)


def gerar_token(id_usuario : int):
  expiracao = datetime.now(timezone.utc) + timedelta(minutes = float(expiracao_token))
  
  info = {"sub": str(id_usuario), "exp": expiracao}
  
  token = jwt.encode(info, chave_secreta, algorithm=os.getenv("ALGORITHM"))
  
  return token