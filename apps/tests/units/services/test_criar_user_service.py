from apps.backend.services.services_users  import gerenciador_user
from apps.backend.schemas.Schema import usuarioSchema
import pytest

# CASOS DE TESTE: Cadastro de usuario

def test_criar_usuario_valida_service_retorna_mesmo_dict_correto(mocker):
  
  """
  Given: Schema valido de nome, e-mail, e senha e repostitory é mockado.
  When: Service_criar_user é chamado para registrar a credenciais do usuario
  Then: Service retorna dict com {id_usuario: 32, nome: Gustavo e email: email@outlook.com}
  """
  

  # Arrange (Preparação)
  Schema_user_pydantic = usuarioSchema(nome_usuario = "Gustavo", 
                              email="email@outlook.com", 
                              senha="123")
  
  resultado_repo= {"id_usuario" : 32,
                  "nome" : "Gustavo",
                  "email" : "",
                  "senha_hash" : "hash-falso"}
  
  mocker.patch("apps.backend.repository.User_Repository.User_Repository.criar_usuario", return_value = resultado_repo)
  
  
  # ACT
  resultado_cadastro = gerenciador_user.service_criar_user(Schema_user_pydantic)
  
  
  # ASSERT
  assert resultado_cadastro == resultado_repo  
  


def test_transforma_senha_em_hash_no_service_cadastro(mocker):
  
  """
  Given: Schema valido de nome, e-mail, e senha hash de senha é mockado.
  When: Service_criar_user é chamado para registrar a credenciais do usuario
  Then: Service_criar user chama transforma_senha_hash uma vez
  """
    
  # ARRANGE 
  Schema_user_pydantic = usuarioSchema(nome_usuario = "wesley", 
                              email="wesley.arruda1@geradornv.com", 
                              senha="123")
  
  mock_hash = mocker.patch("apps.backend.services.services_users.transforma_senha_hash",
                      return_value = "HASH_FAKE")
  
  # ACT
  gerenciador_user.service_criar_user(Schema_user_pydantic)
  
  # ASSERT
  mock_hash.assert_called_once()
  


def test_impede_usuario_usar_mesmo_email_no_cadastro(mocker):
  
  """
  Given: Schema valido de nome, e-mail, e função verificar_usuario_email é mockado.
  When: Service_criar_user é chamado para registrar a credenciais do usuario
  Then: Service_criar user chama verificar_usuario_email uma vez
  """


  # ARRANGE
  Schema_cadastro = usuarioSchema(nome_usuario= "jhonata",
                                  email = "jhonata.leandro174@gmail.com",
                                  senha= "senhaa")

  mocker.patch("apps.backend.repository.User_Repository.User_Repository.verificar_usuario_email", return_value = True)
  
  
  mocker.patch("apps.backend.repository.User_Repository.User_Repository.criar_usuario", return_value = Schema_cadastro)  
  
  
  #  ACT + ASSERT
  with pytest.raises(Exception, match = "Este e-mail já está cadastrado. Tente fazer login"):
    gerenciador_user.service_criar_user(Schema_cadastro)
  