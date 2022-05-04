while True:

    print("Menu de opções")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    print("4 - Exercício 4")
    print("5 - Exercício 5")
    print("6 - Exercício 6")
    print("7 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        #Exercício 1
        tabuada = 5
        print("Tabuada do",tab)
        for x in range(10):
            print(tab,"x", x,"=",tabuada * x)

    elif opcao == 2:
        #Exercício 2
        numero = int(input("Entre com um número inteiro: "))
        for cont in range(0,10):
            numero+=1
            print(numero)

    elif opcao == 3:
        #Exercício 3
        for cont in range(100,201,2):
            print(cont)

    elif opcao == 4:
        #Exercício 4
        num1 = int(input("Digite 1 número inteiro: "))
        num2 = int(input("Digite outro número inteiro: "))
        cont = 0
        if num1 > num2:
            num1,num2 = num2,num1

        num1+=1
        for numero in range(num1,num2):
            if numero % 2 != 0:
                cont+=1
        print("Quantidade de ímpares: ",cont)

    elif opcao == 5:
        #Exercicio 5
        numero1 = int(input("Entre com o primeiro número: "))
        numero2 = int(input("Entre com o segundo número: "))
        soma = 0
        if numero1 > numero2:
            aux = numero1
            numero1 = numero2
            numero2 = aux

        for cont in range(numero1+1,numero2):
            soma+=cont

        print("Soma dos elementos existentes: ",soma)

    elif opcao == 6:
        #Exercício 6
        soma = 0
        qtde = 5

        for cont in range(0,qtde):
            print("Entre com a {}a. idade".format(cont + 1))
            idade = int(input("--> "))
            while idade < 0:
                print("Idade inválida. Digite novamente a {}a. idade".format(cont+1))
                idade = int(input("--> "))
            cont+=10
            soma += idade
        print("Média: ",soma/qtde)

    elif opcao == 7:
        break

    else:
        print("Opção Inválida!")


