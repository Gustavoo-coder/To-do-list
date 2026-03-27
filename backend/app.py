from services.crud import gerenciador_tarefas_crud

# Fluxo crud do to-do-list
while True:
  
  gerenciador_tarefas_crud.menu_opcoes()
  
  escolha_opcoes_crud = input("Escolha a opção: ")
  
  match escolha_opcoes_crud:
    
    case "1":
     gerenciador_tarefas_crud.adicionar_tarefas()
      
    case "2":
      gerenciador_tarefas_crud.visualizar_tarefa()
      
    case "3":
      gerenciador_tarefas_crud.atualizar_tarefa()
    
    case "4":
      gerenciador_tarefas_crud.deletar_tarefa()
    
    case "5":
      print("Saindo do menu de tarefas...")
      break