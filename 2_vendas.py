# 2 - Vendas - Responsáveis Fernando e Thiago.

# (NOTA: As variáveis a seguir são só de exemplo para testar, vou alterar depois!)
menuGeral = 2
if menuGeral == 2:
    import os
    os.system("cls")


    produtos = {"arroz": 6, "feijão": 8, "macarrão": 12, "sal": 2, "açúcar": 3}    #Dicionário com todos os produtos
    qtdProdutos = len(produtos)

    index = 0    #Referência para saber qual é a posição da lista



#ADICIONANDO PRODUTOS AO CARRINHO - ok
    carrinho = {}
    menuEscolha = 1
    while menuEscolha == 1:
        print("Veja a seguir nosso catálogo de produtos: \n")
        while qtdProdutos > 0:   #Listando cada produto
            print(list(produtos)[index].title())
            print("Preço: R$",float(list(produtos.values())[index]))
            print("\n")
            index = index +1
            qtdProdutos = qtdProdutos -1

        escolha = input("Informe o produto que deseja adicionar ao carrinho: ")
        while str(escolha).lower() not in produtos:    # SÓ USAR LOWER SE FOR TUDO LOWER NOS PRODUTOS
            print("\nProduto inválido.")
            escolha = input("Informe um nome válido: ")  
        escolha = escolha.lower()    #Produto escolhido definido.


        qtdEscolha = (input("Informe a quantidade desejada: "))

        while str(qtdEscolha).isnumeric() is not True or int(qtdEscolha) < 1:
            print("\nQuantidade inválida.")
            qtdEscolha = (input("Informe uma quantidade válida: "))
        qtdEscolha = int(qtdEscolha)   #Quantidade escolhida definida.

        carrinho[escolha] = qtdEscolha    #Adiciona ao carrinho

        questaoCarrinho = input("\nDeseja adicionar mais produtos ao carrinho? Digite SIM ou NÃO: ")
        while questaoCarrinho.lower() != "sim" and questaoCarrinho.lower() != "não":
            print("\nResposta inválida.")
            questaoCarrinho = input("Digite SIM ou NÃO: ")
        print("\n")

        if questaoCarrinho.lower() == "sim":
            menuEscolha = 1
            qtdProdutos = len(produtos)   #Loop da lista ativo
            index = 0
            os.system("cls")
        elif questaoCarrinho.lower() == "não":
            menuEscolha = 0
            os.system("cls")

            print("Resumo da compra:")
            countCarrinho = len(carrinho)
            index = 0
            total = 0
            while countCarrinho > 0:
                print("\n")
                print((list(carrinho)[index]).title())
                print("Quantidade:", list(carrinho.values())[index])
                print("Preço: R$", float(produtos[list(carrinho)[index]]))
                countCarrinho = countCarrinho -1
                total = total + produtos[list(carrinho)[index]]
                index = index +1
            print("\n Total a pagar: R$", float(total))


#FINALIZANDO A COMPRA
    questaoRemover = 0
    questaoRemover = input("\nDeseja remover algum item do carrinho? Digite SIM ou NÃO: ")

    while questaoRemover.lower() != "sim" and questaoRemover.lower() != "não":
        print("\nResposta inválida.")
        questaoRemover = input("Digite SIM ou NÃO: ")
    print("\n")

    if questaoRemover.lower() == "sim":
        questaoRemover = 1
    elif questaoRemover.lower() == "não":
        questaoRemover = 0
        menuEscolha = 2    #finalizar

    while questaoRemover == 1:    #Removendo produtos
        remover = input("Informe o nome do produto que deseja remover: ")
        while str(remover).lower() not in carrinho:
            print("\nProduto inválido.")
            remover = input("Informe um nome válido: ")

        carrinho.pop(f'{remover}')
        os.system("cls")
        print(remover.title(), "removido com sucesso!")    #Removido
        
        questaoRemover = input("\nDeseja remover outro produto? Digite SIM ou NÃO: ")    #Repete?
        while questaoRemover.lower() != "sim" and questaoRemover.lower() != "não":    #check
            print("\nResposta inválida.")
            questaoRemover = input("Digite SIM ou NÃO: ")

        if questaoRemover.lower() == "sim":
            questaoRemover = 1
            os.system("cls")

            countCarrinho = len(carrinho)
            index = 0
            total = 0
            print("CARRINHO:")
            while countCarrinho > 0:    #Print do carrinho
                print("\n")
                print((list(carrinho)[index]).title())
                print("Quantidade:", list(carrinho.values())[index])
                print("Preço:", produtos[list(carrinho)[index]])
                countCarrinho = countCarrinho -1
                total = total + produtos[list(carrinho)[index]]
                index = index +1

            print("\n Novo total: R$", float(total))
            print("\n")

            if total == 0:
                    print("\nSeu carrinho está vazio.")
                    enter = input("Aperte Enter para voltar ao início.")
                    menuEscolha = 0
                    questaoRemover = 0

        elif questaoRemover.lower() == "não":
            questaoRemover = 0
            menuEscolha = 2    #finalizar


if menuEscolha == 2:
    os.system("cls")
    countCarrinho = len(carrinho)
    index = 0
    total = 0
    print("CARRINHO:")
    while countCarrinho > 0:    #Print do carrinho
        print("\n")
        print((list(carrinho)[index]).title())
        print("Quantidade:", list(carrinho.values())[index])
        print("Preço:", produtos[list(carrinho)[index]])
        countCarrinho = countCarrinho -1
        total = total + produtos[list(carrinho)[index]]
        index = index +1
    print("\n Total a pagar: R$", float(total))

    enter = input("\nAperte Enter para finalizar a compra.")
    os.system("cls")
    print("Compra efetuada com sucesso!")
    enter = input("\n(Aperte Enter para voltar ao início)")

    
if menuEscolha == 0:
    os.system("cls")
    #Para voltar ao menu inicial