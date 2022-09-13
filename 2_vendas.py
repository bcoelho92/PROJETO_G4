# 1 - Vendas - responsável Fernando

import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

carrinho = {} #Definir essa variável no começo do programa
produtos = {"arroz": 6, "feijão": 8, "macarrão": 12, "sal": 2, "açúcar": 3} #Dicionário com todos os produtos
qtdProdutos = len(produtos)

total_local = 0
menuGeral = 2 #Variável de exemplo para começar meu código
menuVendas = 0
while menuGeral == 2:

    if int(menuVendas) == 0: #Menu de Vendas
        clear()
        print('''\n
    MENU DE VENDAS

    1 - Adicionar produtos ao carrinho
    2 - Remover produtos do carrinho
    3 - Carrinho
    4 - Voltar ao início
    ''')
        menuVendas = input("Digite a opção desejada: ")
        while str(menuVendas).isnumeric() != True or str(menuVendas) not in "1234":#check
            print("\nResposta inválida.")
            menuVendas = input("Digite uma opção válida: ")


    if int(menuVendas) == 1: #Adicionar
        clear()
        print("Veja a seguir nosso catálogo de produtos: \n")
        index = 0 #Referência para posição
        qtdProdutos = len(produtos)
        while qtdProdutos > 0: #Print: lista de produtos
            print(list(produtos)[index].title())
            print("Preço: R$",float(list(produtos.values())[index]))
            print("\n")
            index = index +1
            qtdProdutos = qtdProdutos -1

        escolha = input("Informe o produto que deseja adicionar ao carrinho: ")
        while str(escolha).lower() not in produtos: #check LOWER!
            print("\nProduto inválido.")
            escolha = input("Informe um nome válido: ")  
        escolha = escolha.lower() #Produto escolhido definido.

        qtdEscolha = (input("Informe a quantidade desejada: "))
        while str(qtdEscolha).isnumeric() is not True or int(qtdEscolha) < 1:#check
            print("\nQuantidade inválida.")
            qtdEscolha = (input("Informe uma quantidade válida: "))
        qtdEscolha = int(qtdEscolha) #Quantidade escolhida definida.


        carrinho[escolha] = qtdEscolha #Adiciona ao carrinho
        carrinhoAdicionar = input("\nDeseja adicionar mais produtos ao carrinho? Digite SIM ou NÃO: ")
        while carrinhoAdicionar.lower() != "sim" and carrinhoAdicionar.lower() != "não": #check
            print("\nResposta inválida.")
            carrinhoAdicionar = input("Digite SIM ou NÃO: ")
        print("")

        if carrinhoAdicionar.lower() == "sim":
            menuVendas = 1
            clear()
        elif carrinhoAdicionar.lower() == "não":
            menuVendas = 3
            clear()


    if int(menuVendas) == 2 and total_local == 0:#Remover produtos com carrinho vazio
        clear()
        print("Seu carrinho está vazio.")
        enter = input("\nAperte Enter para retornar ao menu ")
        menuVendas = 0

    if int(menuVendas) == 5 and total_local == 0:#Finalizar compra com carrinho vazio
        clear()
        print("Seu carrinho está vazio.")
        enter = input("\nAperte Enter para retornar ao menu ")
        menuVendas = 0

    
    if int(menuVendas) == 2 and total_local > 0:#Remover produtos do carrinho
        clear()
        print("CARRINHO") #Print carrinho
        countCarrinho = len(carrinho)
        index = 0
        total_local = 0
        while countCarrinho > 0:
            print("\n")
            print((list(carrinho)[index]).title())
            print("Quantidade:", list(carrinho.values())[index])
            print("Preço: R$", float(produtos[list(carrinho)[index]]))
            countCarrinho = countCarrinho -1
            total_local = total_local + produtos[list(carrinho)[index]]
            index = index +1
        print("\n Total a pagar: R$", float(total_local))#>

        prodRemovido = input("\nInforme o nome do produto que deseja remover: ")
        while str(prodRemovido).lower() not in carrinho: #check LOWER?
                print("\nProduto inválido.")
                prodRemovido = input("Informe um nome válido: ")

        carrinho.pop(f'{prodRemovido}')
        prodRemovido = prodRemovido.lower()#check LOWER?
        total_local = total_local - float(produtos[f'{prodRemovido}'])
        clear()
        print(prodRemovido.title(), "removido com sucesso!") #Removido
            
        questaoRemover = input("\nDeseja remover outro produto? Digite SIM ou NÃO: ") #Repete?
        while questaoRemover.lower() != "sim" and questaoRemover.lower() != "não":#check
                print("\nResposta inválida.")
                questaoRemover = input("Digite SIM ou NÃO: ")

        if questaoRemover.lower() == "sim":
            menuVendas = 2

            if total_local == 0:
                print("\nSeu carrinho está vazio.")
                enter = input("\n Aperte Enter para voltar ao início.")
                menuVendas = 0
        elif questaoRemover.lower() == "não":
            menuVendas = 3


    if int(menuVendas) == 3: #Carrinho
        clear()

        print("CARRINHO") #Print carrinho
        countCarrinho = len(carrinho)
        index = 0
        total_local = 0
        while countCarrinho > 0:
            print("\n")
            print((list(carrinho)[index]).title())
            print("Quantidade:", list(carrinho.values())[index])
            print("Preço: R$", float(produtos[list(carrinho)[index]]))
            countCarrinho = countCarrinho -1
            total_local = total_local + produtos[list(carrinho)[index]]
            index = index +1
        print("\n Total a pagar: R$", float(total_local))#>

        print('''\n
        1 - Adicionar produtos ao carrinho
        2 - Remover produtos do carrinho
        5 - Finalizar a compra

        0 - Voltar ao menu
        ''')
        menuVendas = input("\nDigite a opção desejada: ")
        while str(menuVendas).isnumeric() != True or str(menuVendas) not in "1250":#check
            print("Opção inválida!")
            menuVendas = input("Digite novamente: ")

        if int(menuVendas) == 5 and total_local != 0: #Finalizar compra
            clear()
            print("CARRINHO") #Print carrinho
            countCarrinho = len(carrinho)
            index = 0
            total_local = 0
            while countCarrinho > 0:
                print("\n")
                print((list(carrinho)[index]).title())
                print("Quantidade:", list(carrinho.values())[index])
                print("Preço: R$", float(produtos[list(carrinho)[index]]))
                countCarrinho = countCarrinho -1
                total_local = total_local + produtos[list(carrinho)[index]]
                index = index +1
            print("\n Total a pagar: R$", float(total_local))#>

            enter = input("\nAperte Enter para confirmar a compra")
            clear()
            print("Compra efetuada com sucesso!")
            vendasQtd = carrinho
            enter = input("\nAperte Enter para voltar ao menu inicial")
            carrinho = {}
            menuVendas = 0


if menuVendas == 4:
    menuGeral = 0