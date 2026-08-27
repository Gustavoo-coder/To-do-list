from pwdlib import PasswordHash

senha_hash = PasswordHash.recommended()


# trasnformar senha em hash
def transforma_senha_hash(senha:str) -> str:
  return senha_hash.hash(senha)

# verifca senha fornecida
def verificar_senha(senha_login: str,  senha_banco:str):
  return senha_hash.verify(senha_login,senha_banco)