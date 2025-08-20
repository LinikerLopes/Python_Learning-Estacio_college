#Projeto de CRUD

tarefas = []
opcao = True
message = "Olá, seja bem vindo"

print(message)

while opcao:
    print("1 - Adicionar tarefa")
    print("2 - Atualizar tarefa")
    print("3 - Remover tarefa")
    print("4 - Listar tarefas")
    print("0 - Sair")

    escolha = int(input("Escolha uma opcao: "))

    match escolha:
        case 1:
            print("=================================")
            tarefas.append(input("Digite a tarefa: "))
            print("Lista atual:")
            for i, item in enumerate(tarefas):
              print(f"{i+1}: {item}")
            print("=================================")
        case 2:
             print("=================================")
             pos = int(input("Digite a posição do item que deseja atualizar: "))
             print("Lista atual:")
             for i, item in enumerate(tarefas):
              print(f"{i+1} - {item}")
             if 0 <= pos <= len(tarefas):
                novo = input("Digite o novo valor: ")
                tarefas[pos-1] = novo
                print("Item atualizado!")
             else:
                print("Posição inválida.")
             print("=================================")

        case 3:
            print("=================================")
            print("Lista atual:")
            for i, item in enumerate(tarefas):
              print(f"{i+1}: {item}")

            pos = int(input("Digite a posição do item que deseja remover: "))
            if 0 <= pos <= len(tarefas):
                removido = tarefas.pop(pos-1)
                print(f"Item '{removido}' removido!")
            else:
                print("Posição inválida.")
            print("=================================")

        case 4:
            print("=================================")
            print("Lista atual:")
            for i, item in enumerate(tarefas):
             print(f"{i+1}: {item}")
            print("=================================")
        case 0:
            print("=================================")
            print("Saindo...")
            opcao = False
            print("=================================")
        case _:
            print("=================================")
            print("Opção inválida")
            print("=================================")