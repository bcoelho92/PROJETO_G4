# 1 - Vendas - responsável Fernando

carrinho = {} #DEFINIR NO COMEÇO DO PROGRAMA

import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


qtdlista = len(lista)

totalCarrinho = 0
menuFernando = 2 #ISSO COMEÇA A RODAR MEU CÓDIGO
menuVendas = 0
while menuFernando == 2:

    if int(menuVendas) == 0: #Menu de Vendas
        clear()
        print(''' 
******************************************
MENU VENDAS 

Essas são as opções do programa:  

[1] - Adicionar produtos ao carrinho
[2] - Remover produtos do carrinho
[3] - Carrinho
[4] - Voltar ao menu anterior

******************************************''')
        menuVendas = input("Digite a opção desejada: ")
        while str(menuVendas).isnumeric() != True or str(menuVendas) not in "1234":#check
            print("\nResposta inválida.")
            menuVendas = input("Digite uma opção válida: ")


    if int(menuVendas) == 1: #Adicionar
        clear()
        print("Veja a seguir nosso catálogo de produtos: \n")
        index = 0 #Referência para posição
        qtdProdutos = len(lista)
        while qtdProdutos > 0: #Print: lista de produtos
            print(list(lista)[index].title())
            print("Preço: R$",float(list(lista.values())[index]))
            print("____________________________________\n")
            index = index +1
            qtdProdutos = qtdProdutos -1

        escolha = input("Informe o produto que deseja adicionar ao carrinho: ")
        while str(escolha).title() not in lista: #check LOWER!
            print("\nProduto inválido.")
            escolha = input("Informe um nome válido: ")  
        escolha = escolha.title() #Produto escolhido definido.

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


    if int(menuVendas) == 2 and totalCarrinho == 0:#Remover produtos com carrinho vazio
        clear()
        print("Seu carrinho está vazio.")
        enter = input("\nAperte Enter para retornar ao menu ")
        menuVendas = 0

    if int(menuVendas) == 5 and totalCarrinho == 0:#Finalizar compra com carrinho vazio
        clear()
        print("Seu carrinho está vazio.")
        enter = input("\nAperte Enter para retornar ao menu ")
        menuVendas = 0

    
    if int(menuVendas) == 2 and totalCarrinho > 0:#Remover produtos do carrinho
        clear()
        print("CARRINHO") #Print carrinho
        countCarrinho = len(carrinho)
        index = 0
        totalCarrinho = 0
        while countCarrinho > 0:
            print((list(carrinho)[index]).title())
            print("Quantidade:", list(carrinho.values())[index])
            print("Preço: R$", float(lista[list(carrinho)[index]]))
            print("____________________________________\n")
            countCarrinho = countCarrinho -1
            totalCarrinho = totalCarrinho + lista[list(carrinho)[index]]
            index = index +1
        print("\n Total a pagar: R$", float(totalCarrinho))#>

        prodRemovido = input("\nInforme o nome do produto que deseja remover: ")
        while str(prodRemovido).title() not in carrinho: #check LOWER?
                print("\nProduto inválido.")
                prodRemovido = input("Informe um nome válido: ")

        carrinho.pop(f'{prodRemovido}')
        prodRemovido = prodRemovido.title()#check LOWER?
        totalCarrinho = totalCarrinho - float(lista[f'{prodRemovido}'])
        clear()
        print(prodRemovido.title(), "removido com sucesso!") #Removido
            
        questaoRemover = input("\nDeseja remover outro produto? Digite SIM ou NÃO: ") #Repete?
        while questaoRemover.lower() != "sim" and questaoRemover.lower() != "não":#check
                print("\nResposta inválida.")
                questaoRemover = input("Digite SIM ou NÃO: ")

        if questaoRemover.lower() == "sim":
            menuVendas = 2

            if totalCarrinho == 0:
                print("\nSeu carrinho está vazio.")
                enter = input("\n Aperte Enter para voltar ao início.")
                menuVendas = 0
        elif questaoRemover.lower() == "não":
            menuVendas = 3


    if int(menuVendas) == 3: #Carrinho
        clear()

        print("CARRINHO:\n") #Print carrinho
        countCarrinho = len(carrinho)
        index = 0
        totalCarrinho = 0
        while countCarrinho > 0:
            print((list(carrinho)[index]).title())
            print("Quantidade:", list(carrinho.values())[index])
            print("Preço: R$", float(lista[list(carrinho)[index]]))
            print("____________________________________\n")
            countCarrinho = countCarrinho -1
            totalCarrinho = totalCarrinho + lista[list(carrinho)[index]]
            index = index +1
        print("\n Total a pagar: R$", float(totalCarrinho))#>

        print(''' 
******************************************
MENU

[1] - Adicionar produtos ao carrinho
[2] - Remover produtos do carrinho
[5] - Finalizar compra

[0] - Voltar ao menu anterior

******************************************''')
        menuVendas = input("\nDigite a opção desejada: ")
        while str(menuVendas).isnumeric() != True or str(menuVendas) not in "1250":#check
            print("Opção inválida!")
            menuVendas = input("Digite novamente: ")

        if int(menuVendas) == 5 and totalCarrinho != 0: #Finalizar compra
            clear()
            print("CARRINHO:\n") #Print carrinho
            countCarrinho = len(carrinho)
            index = 0
            totalCarrinho = 0
            while countCarrinho > 0:
                print((list(carrinho)[index]).title())
                print("Quantidade:", list(carrinho.values())[index])
                print("Preço: R$", float(lista[list(carrinho)[index]]))
                print("____________________________________\n")
                countCarrinho = countCarrinho -1
                totalCarrinho = totalCarrinho + lista[list(carrinho)[index]]
                index = index +1
            print("\n Total a pagar: R$", float(totalCarrinho))#>

            enter = input("\nAperte Enter para confirmar a compra")
            clear()
            print("Compra efetuada com sucesso!")
            vendasQtd = carrinho
            enter = input("\nAperte Enter para voltar ao menu inicial")
            carrinhoRef = carrinho #Referência ao menu de Relatório
            carrinho = {}
            menuVendas = 0


    if int(menuVendas) == 4:
        menuFernando = 0
        menuGeral = ?? #SAIR DO MEU PROGRAMA