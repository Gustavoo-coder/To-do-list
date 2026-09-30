#  testes que tem qe dar erro
import pytest
from apps.tests.exemplos import soma_2, error, saudacao

def test_soma():
  n1 = 2
  n2 = 2
  total = soma_2(n1,n2)
    
  # assert faz a validação se aquilo que afirmamos é o que usamos
  assert total == 4
  assert isinstance(total, int)
  
  


def test_error_pytest(): # mais viavél
 with pytest.raises(Exception, match="ERROR - 500"): # verifca se a função vai soltar uma erro
  error()
  
  
# mockando

def test_saudadcao(mocker):
  # passo o a função que vai ser mockada para uso de teste retornar um valor
  mocker.patch("tests.soma.pegar_nome" , return_value = "Gustavo")
  
  
  saudacao()
