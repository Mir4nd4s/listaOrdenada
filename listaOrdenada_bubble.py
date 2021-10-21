def bubble_sort(lista):
	for i in range(0,len(lista)-1):
		for j in range(len(lista)-1):  
			if(lista[j]>lista[j+1]):  
				temp = lista[j]  
				lista[j] = lista[j+1]  
				lista[j+1] = temp  
	return lista 

opcao = ""

while opcao != "0":
    print("(1) - Ver ranking dos restaurantes")
    print("(2) - Ver ranking das pizzarias")
    print("(0) - Sair do programa")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        restaurantes = [['china in box', 4.5, 0.9],
					   ['ragazzo', 3.9, 1.2],
					   ['mama italia', 4.5, 1.9],
					   ['nippon', 4.0, 0.7], 
					   ['spettus', 3.2, 1.4], 
					   ['forneria', 4.0, 0.2]]

        bubble_sort(restaurantes)

        print('\n# Melhores Restaurantes #')
        for item in restaurantes:
            print(item)

        print("\n ************ FIM! ************ \n")

    if opcao == "2":
        pizzaria = [['di matteo', 4.5, 0.9],
					['pizza hut"s', 3.9, 1.2],
					['massarella', 4.5, 1.9],
					['tradição', 4.0, 0.7], 
					['capitão gancho', 3.2, 1.4], 
					['a fábrica', 4.0, 0.2]]

        bubble_sort(pizzaria)
        
        print('\n# Melhores Pizzarias #')
        for item in pizzaria:
            print(item)

        print("\n ************ FIM! ************ \n")

    elif opcao > "2" or opcao < "0":
        print("\n *** Opção inválida... Tente novamente! ***\n")

print("\n ***** Programa encerrado! *****")
