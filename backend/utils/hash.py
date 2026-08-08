from pwdlib import PasswordHash

senha_hash = PasswordHash.recommended()


# trasnformar senha em hash
def transforma_senha_hash(senha:str) -> str:
  return senha_hash.hash(senha)