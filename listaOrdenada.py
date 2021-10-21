opcao = ""

while opcao != "0":
    print("(1) - Ver ranking dos restaurantes")
    print("(2) - Ver ranking das pizzarias")
    print("(0) - Sair do programa")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        restaurante = ['china in box', 'ragazzo', 'haro', 'habib´s']
        avaliacao = [4.5, 3.6, 4.5, 4.0]
        distancia = [0.2, 0.9, 1.8, 0.9]

        resultado = []

        for i in range(len(restaurante)):
            tupla = (avaliacao[i], restaurante[i], distancia[i])
            resultado.append(tupla)

        resultado.sort(reverse=True)

        print('# Melhores Restaurantes #')
        for item in resultado:
            print(item)


        print("\n ************ FIM! ************ \n")

    if opcao == "2":
        pizzaria = ['pizzaria do Chicão', 'pizzaria Atlantico', 'Di Matteo Pizzaria', 'Pizzaria Passira']
        avaliacao = [4.5, 3.6, 4.5, 4.0]
        distancia = [0.2, 0.9, 1.8, 0.9]

        resultado = []

        for i in range(len(pizzaria)):
            tupla = (avaliacao[i], pizzaria[i], distancia[i])
            resultado.append(tupla)

        resultado.sort(reverse=True)

        print('# Melhores Pizzarias #')
        for item in resultado:
            print(item)

        print("\n ************ FIM! ************ \n")

    elif opcao > "2" or opcao < "0":
        print("\n *** Opção inválida... Tente novamente! ***\n")

print("\n ***** Programa encerrado! *****")