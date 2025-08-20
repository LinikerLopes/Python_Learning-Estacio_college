#Projeto de CRUD

tarefas = []
opcao = True
message = "Olá, seja bem vindo"

print(message)

while opcao:
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefas")
    print("3 - Remover tarefas")
    print("4 - Atualizar tarefa")
    print("0 - Sair")
    choice = (int(input("Digite uma opcao")))

    match choice:
        case 1:
            print("Listando tarefas")
            for tarefa in tarefas:
                print(tarefa)
        case 2:
            print("Adicionando tarefa")
            tarefas.append(input("Digite a tarefa: "))
        case 3:
            print("Removendo tarefa")
        case 4:
            opcao = False