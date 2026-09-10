from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# carrega o .env
load_dotenv()

def conecta_banco():
  
    
  # Faz a montagem da engine
  engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}",
    pool_pre_ping=True
  )

  # Teste da montagem da engine e conexão ao banco
  try:
      with engine.connect():
        print("Conectado com sucesso")
        return engine
  
  except Exception as e:
    print("Erro ao conectar no banco ❌")
    print(f"Erro: {e}")

