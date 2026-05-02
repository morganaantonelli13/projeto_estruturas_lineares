fila = []

while True:
    print("\nSECRETARIA ACADÊMICA")
    print("[1] - Retirar senha")
    print("[2] - Chamar próximo aluno")
    print("[3] - Mostrar fila")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        fila.append(nome)
        print(f"{nome} entrou na fila de atendimento.")

    elif opcao == "2":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            proximo = fila.pop(0)
            print(f"Chamando aluno: {proximo}")

    elif opcao == "3":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            print("Fila atual:")
            for i in range(len(fila)):
                print(f"{i + 1}º - {fila[i]}")

    elif opcao == "4":
        break