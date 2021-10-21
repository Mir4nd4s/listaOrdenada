opcao = ""

while opcao != "0":
    print("(1) - Ver ranking dos restaurantes")
    print("(2) - Ver ranking das pizzarias")
    print("(0) - Sair do programa")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        restaurantes = [[4.5, 'china in box', 0.9],
					   [3.9, 'ragazzo', 1.2],
					   [4.5, 'mama italia', 1.9],
					   [4.0, 'nippon', 0.7], 
					   [3.2, 'spettus', 1.4], 
					   [4.0, 'forneria', 0.2]]

        restaurantes.sort(reverse=True)

        print('\n# Melhores Restaurantes #')
        for item in restaurantes:
            print(item[1], '\navaliação ★ {} \ndistancia: {}km\n____________________' 
				  .format(item[0],item[2]))

        print("\n ************ FIM! ************ \n")

    if opcao == "2":
        pizzaria = [[4.5, 'di matteo', 0.9],
					[3.9, 'pizza hut"s', 1.2],
					[3.0, 'massarella', 1.9],
					[4.0, 'tradição', 0.7], 
					[3.2, 'capitão gancho', 1.4], 
					[4.0, 'a fábrica', 0.2]]

        pizzaria.sort(reverse=True)
        
        print('\n# Melhores Pizzarias #')
        for item in pizzaria:
            print(item[1], '\navaliação ★ {} \ndistancia: {}km\n____________________' 
				  .format(item[0],item[2]))

        print("\n ************ FIM! ************ \n")

    elif opcao > "2" or opcao < "0":
        print("\n *** Opção inválida... Tente novamente! ***\n")

print("\n ***** Programa encerrado! *****")
