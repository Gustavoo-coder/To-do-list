#importar função externa
# from services.regras import menu_opcoes
# from services.regras import adicionar_tarefas
# from services.regras import visualizar_tarefa
# from services.regras import atualizar_tarefa
# from services.regras import deletar_tarefa


from services.regras import(
  menu_opcoes,
  adicionar_tarefas,
  visualizar_tarefa,
  atualizar_tarefa,
  deletar_tarefa
)

# Fluxo crud do to-do-list
while True:
  
  menu_opcoes()
  
  escolha_opcoes_crud = input("Escolha a opção: ")
  
  match escolha_opcoes_crud:
    
    case "1":
      adicionar_tarefas()
      
    case "2":
      visualizar_tarefa()
      
    case "3":
      atualizar_tarefa()
    
    case "4":
      deletar_tarefa()
    
    case "5":
      print("Saindo do menu de tarefas...")
      break