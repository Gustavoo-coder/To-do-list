from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

driver = "postgresql+psycopg2"
user = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

URL_engine = (
  f"{driver}://{user}:{senha}@{host}:{port}/{database}"
)

print("Montando Engine....")
create_engine(URL_engine)
print("Engine criada com sucesso...")
print(URL_engine)
