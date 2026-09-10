from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

print("1 - iniciou")

# carrega o .env
load_dotenv()

print("2 - carregou .env")

print("USER:", os.getenv("DB_USER"))
print("HOST:", os.getenv("DB_HOST"))
print("PORT:", os.getenv("DB_PORT"))
print("NAME:", os.getenv("DB_NAME"))

def conecta_banco():
  
  print("3 - entrou na função")

  # Faz a montagem da engine
  engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}",
    pool_pre_ping=True
  )
  
  print("4 - criou engine")

  # Teste da montagem da engine e conexão ao banco
  try:
      with engine.connect():
        print("Conectado com sucesso")
        return engine
  
  except Exception as e:
    print("Erro ao conectar no banco ❌")
    print(f"Erro: {e}")


conecta_banco()