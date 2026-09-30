
def soma_2(a:int,b:int) -> int:
  return a + b

def error():
  raise Exception("ERROR - 500")


# usando mock


def pegar_nome():
  nome = input("Digite seu nome: ")
  
  return nome

def saudacao():
  nome_saudacao = pegar_nome()
  
  print(f"Ola {nome_saudacao} seja bem vindo ao nosso curso !")

