pilha = []

while True:
    print("\nEDITOR DE TEXTO")
    print("[1] - Digitar palavra")
    print("[2] - Desfazer última palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        palavra = input("Digite uma palavra: ")
        pilha.append(palavra)
        print(f"Palavra adicionada: {palavra}")

    elif opcao == "2":
        if len(pilha) == 0:
            print("Nada para desfazer. O texto está vazio.")
        else:
            removida = pilha.pop()
            print(f"Palavra removida: {removida}")

    elif opcao == "3":
        if len(pilha) == 0:
            print("O texto está vazio.")
        else:
            print("Texto atual: " + " ".join(pilha))

    elif opcao == "4":
        break