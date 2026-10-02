# CASOS DE TESTE: Cadastro de usuario
from apps.backend.services.services_users  import gerenciador_user
from apps.backend.schemas.Schema import usuarioSchema


def test_criar_usuario_valida_service_retorna_mesmo_dict_correto(mocker):
  
  # Arrange (Preparação)
  Schema_user_pydantic = usuarioSchema(nome_usuario = "Gustavo", 
                              email="Gustavoaft78@outlook.com", 
                              senha="Aft261278@$")
  
  resultado_repo= {"id_usuario" : 32,
                  "nome" : "Gustavo",
                  "email" : "Gustavoaft78@outlook.com",
                  "senha_hash" : "hash-falso"}
  
  mocker = mocker.patch("apps.backend.repository.User_Repository.User_Repository.criar_usuario", return_value = resultado_repo)
  
  
  # ACT
  resultado_cadastro = gerenciador_user.service_criar_user(Schema_user_pydantic)
  
  
  # ASSERT
  assert resultado_cadastro == resultado_repo  
  
  