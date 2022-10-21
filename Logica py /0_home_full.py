####################################################################################

# Boas vindas / 0 - Menu
# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Bruno 
# 1 - Cadastro - Julia 
# 2 - Vendas - Fernando
# 3 - Relatorio - Fernando

####################################################################################

# Boas vindas / 0 - Menu

import sys
import os

# VARIAVEIS 

menuGeral = 0
menuCad = 0
menuVendas = 0
menuRelat = 0

print()
nomeCliente = str(input('''
******************************************
Bem vindo(a) ao sistema de cadastro e vendas da Organico’s!

Por favor digite seu nome: '''))
nomeCliente = nomeCliente.title()
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("\n")

descm0 ='''
******************************************
{}, este é o menu principal.

Essas são as opções :           
                                                     
[1] - Cadastro                                 
[2] - Vendas                                   
[3] - Relatório                                
[4] - Sair                                     
                                                     
****************************************** '''
descm1 =''' 
******************************************
Bem vindo(a) ao Menu de Estoque! 

{}, essas são as opções:  

[1] - Cadastramento de produtos
[2] - Listar produtos cadastrados
[3] - Apagar um Produto do Cadastro

[4] - Sair    

******************************************'''
descm2b = '''
Bem vindo(a) ao Menu de Carrinho! 

{}, essas são as opções: 

[1] - Adicionar produtos ao carrinho
[2] - Remover produtos do carrinho
[5] - Finalizar compra

[0] - Voltar ao menu anterior

'''
descm2 =''' 
******************************************
Bem vindo(a) ao Menu de Vendas! 

{}, essas são as opções: 

[1] - Adicionar produtos ao carrinho
[2] - Remover produtos do carrinho
[3] - Finalizar compra

[4] - Voltar ao menu anterior

******************************************'''  
descm3 =''' 
******************************************
Bem vindo(a) ao Menu de Relatório! 

{}, essas são as opções: 

[1] - Quantidade vendida por produto
[2] - Total vendido por produto (em reais)
[3] - Total vendido (em reais)

[4] - Voltar ao menu anterior   

******************************************'''

lista = {} #lista vazia
carrinho = {} #Definir essa variável no começo do programa
carrinhoRef = {}
# qtdlista = 0

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check_quantidade(num): #Checa se a qtd. é um número maior que 0
    while str(num).isnumeric() is not True or int(num) < 1:
        print("\nQuantidade inválida.")
        num = (input("Informe uma quantidade válida: "))
    return int(num)

def check_SouN(x):
    while x.lower() != "s" and x.lower() != "n":
        print("\nResposta inválida.")
        x = input("Digite S (sim) ou N (não): ")
    return str(x)

def print_carrinho():
    print("CARRINHO\n")
    countCarrinho = len(carrinho)
    index = 0
    totalCarrinho = 0
    while countCarrinho > 0:
        print((list(carrinho)[index]).title())
        print("Quantidade:", list(carrinho.values())[index])
        print("Preço: R$", float(lista[list(carrinho)[index]]))
        print("____________________________________\n")
        countCarrinho = countCarrinho -1
        somacar = lista[list(carrinho)[index]] 
        totalCarrinho = totalCarrinho + (float(somacar)*list(carrinho.values())[index])
        index = index +1
    print("\n   Total a pagar: R$", float(totalCarrinho))#>
    print("____________________________________\n")


# def main():
while True:
    print(descm0.format(nomeCliente))
    menuGeral = int(input('{}, digite a opção: '.format(nomeCliente)))
    print()

    if menuGeral == 1:
        clear()
        while True:
            print (descm1.format(nomeCliente))
            print('')
            menuCad = int(input('Digite a opção desejada: '))

            while menuCad >=5 or menuCad <=0:
                menuCad = int(input('Digite uma opção válida: '))

            if menuCad == 1:
                clear()
                qtd = input("\nQuantos produtos você gostaria de adicionar? ")
                while str(qtd).isnumeric() != True:
                    print("\nQuantidade inválida!")
                    qtd = input("Quantos produtos você gostaria de adicionar?\n")
                qtd = int(qtd)

                for i in range(qtd):
                    produto = input("Digite o nome do produto: ").title()
                    valor = input("Digite o valor do produto: ")
                    print("\n")
                    lista[produto] = valor
                clear()
            
            elif menuCad == 2:
                clear()
                print("Esses são os produtos cadastrados no estoque:\n") 
                print("Produtos cadastrados:")
                for produto in lista:
                    print("-", (produto), "R$",(valor))

            elif menuCad == 3:
                clear()
                #remover item cadastrado
                deleta = input("Qual produto você gostaria de deletar? Digite ENTER para reexibir a lista: ").title()
                if deleta in lista:
                    lista.pop(deleta)
                    print ("\nVocê apagou o item: \n-", (deleta), "\n")
                    print("\nLista Atualizada:")
                    print(lista)
                elif deleta == "":
                    print(lista)
                else: print("\nProduto nao cadastrado!")

            elif menuCad == 4:
                clear()
                print("Saindo do Menu de Cadastro\n")
                break
        
    elif menuGeral == 2:
        qtdlista = len(lista)
        totalCarrinho = 0

        while True:
            if int(menuVendas) == 0: #Menu de Vendas
                clear()
                print(descm2.format(nomeCliente))
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

                escolha = input("Informe o produto que deseja adicionar ao carrinho ou aperte 0 para voltar ao menu: ")
                
                if str(escolha) in "0":
                    menuVendas = 0
                else:
                    while str(escolha).title() not in lista:
                        print("\nProduto inválido.")
                        escolha = input("Informe um nome válido: ")  
                    escolha = escolha.title() #Produto escolhido definido.
                
                    qtdEscolha = (input("Informe a quantidade desejada: "))
                    qtdEscolha = check_quantidade(qtdEscolha)


                    carrinho[escolha] = qtdEscolha #Adiciona ao carrinho
                    carrinhoAdicionar = input("\nDeseja adicionar mais produtos ao carrinho? Digite S (sim) ou N (não): ")
                    carrinhoAdicionar = check_SouN(carrinhoAdicionar)
                    print("")

                    if carrinhoAdicionar.lower() == "s":
                        menuVendas = 1
                        clear()
                    elif carrinhoAdicionar.lower() == "n":
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
                print_carrinho()

                prodRemovido = input("\nInforme o nome do produto que deseja remover: ")
                while str(prodRemovido).title() not in carrinho:
                        print("\nProduto inválido.")
                        prodRemovido = input("Informe um nome válido: ")
                clear()     
                carrinho.pop(f'{prodRemovido.title()}')
                prodRemovido = prodRemovido.title()
                totalCarrinho = totalCarrinho - float(lista[f'{prodRemovido}'])
                
                print(prodRemovido.title(), "removido com sucesso!") #Removido
                    
                questaoRemover = input("\nDeseja remover outro produto? Digite S ou N: ") #Repete?
                questaoRemover = check_SouN(questaoRemover)

                if questaoRemover.lower() == "s":
                    menuVendas = 2

                    if totalCarrinho == 0:
                        print("\nSeu carrinho está vazio.")
                        enter = input("\n Aperte Enter para voltar ao início.")
                        menuVendas = 0
                elif questaoRemover.lower() == "n":
                    menuVendas = 3


            if int(menuVendas) == 3: #Carrinho
                clear()
                print_carrinho()

                print(descm2b.format(nomeCliente))
                menuVendas = input("\nDigite a opção desejada: ")
                while str(menuVendas).isnumeric() != True or str(menuVendas) not in "1250":#check
                    print("Opção inválida!")
                    menuVendas = input("Digite novamente: ")

                if int(menuVendas) == 5 and totalCarrinho != 0: #Finalizar compra
                    clear()
                    print_carrinho

                    enter = input("\nAperte Enter para confirmar a compra")
                    clear()
                    print("Compra efetuada com sucesso!")
                    vendasQtd = carrinho
                    enter = input("\nAperte Enter para voltar ao menu inicial")
                    carrinhoRef = carrinho #Referência ao menu de Relatório
                    carrinho = {}
                    menuVendas = 0


            if int(menuVendas) == 4:
                clear()
                break

    elif menuGeral == 3:
        print (descm3.format(nomeCliente))
        print()
        
        menuRelatorio = 0
        vendasValor = lista #lista com o produto e seu preço (na lista de produtos)

        #Adicionando todos os produtos da lista à lista quantidade vendidas:
        indexVendas = 0
        countProdutos = len(lista)
        vendasQuant = {}
        while countProdutos > 0:
            nomeProd = list(lista)[indexVendas]
            vendasQuant[nomeProd] = 0
            indexVendas = indexVendas +1
            countProdutos = countProdutos -1#>

        while menuGeral == 3:

            #CHECK - OPÇÃO 1 - Somando itens do carrinho ao relatório de vendas (sem prints)
            count = len(carrinhoRef)
            indexSoma = 0
            while count > 0:
                nomeProd = list(carrinhoRef)[indexSoma]
                quantProduto1 = carrinhoRef[nomeProd]
                quantProduto2 = vendasQuant[nomeProd]
                novaQuant = quantProduto1 + quantProduto2
                vendasQuant[nomeProd] = novaQuant
                indexSoma = indexSoma+1
                count = count-1
                carrinhoRef[nomeProd] = 0

            #CHECK - OPÇÃO 2 - Referenciar o dicionário de lista.
            index = 0
            countVendasValor = len(lista)
            totalTotal = 0
            while countVendasValor > 0:
                nomeProdutoVendido = (list(lista)[index])
                quantProdutoVendido = vendasQuant[nomeProdutoVendido]
                precoProdutoVendido = lista[nomeProdutoVendido]
                totalProdutoVendido = (int(quantProdutoVendido)*float(precoProdutoVendido))
                totalTotal = totalTotal +totalProdutoVendido
                index = index +1
                countVendasValor = countVendasValor = countVendasValor -1

            if int(menuRelatorio) == 0:
                clear()
                print(descm3.format(nomeCliente))

                menuRelatorio = input("Digite a opção desejada: ")
                while str(menuRelatorio) not in "1234" or str(menuRelatorio).isnumeric() != True:
                    print("\nOpção inválida")
                    menuRelatorio = input("Digite uma opção válida: ")


            if int(menuRelatorio) == 1: #Quantidade vendida de cada produto.
                clear()
                count = len(carrinhoRef)
                indexSoma = 0
                while count > 0: #Somando itens do carrinho ao relatório de vendas
                    nomeProd = list(carrinhoRef)[indexSoma]
                    quantProduto1 = carrinhoRef[nomeProd] #Quantidade no carrinho
                    quantProduto2 = vendasQuant[nomeProd] #Quantidade na lista de vendas
                    novaQuant = quantProduto1 + quantProduto2
                    vendasQuant[nomeProd] = novaQuant

                    indexSoma = indexSoma+1
                    count = count-1

                    print(nomeProd.title())
                    print("Quantidade vendida: ",novaQuant)
                    print("____________________________________\n")

                    carrinhoRef[nomeProd] = 0

                enter = input("Aperte Enter para voltar")
                menuRelatorio = 0
            
            if int(menuRelatorio) == 2: #Valor vendido de cada produto.
                clear()
                index = 0
                countVendasValor = len(lista) #Referenciar o dicionário de produtos.
                totalTotal = 0
                while countVendasValor > 0:
                    print((list(lista)[index]).title())
                    print("Preço por unidade: R$",list(lista.values())[index])
                    nomeProdutoVendido = (list(lista)[index])
                    quantProdutoVendido = vendasQuant[nomeProdutoVendido]
                    precoProdutoVendido = lista[nomeProdutoVendido]
                    totalProdutoVendido = (int(quantProdutoVendido)*float(precoProdutoVendido))
                    totalTotal = totalTotal +totalProdutoVendido
                    print("Total vendido: R$",totalProdutoVendido)
                    print("____________________________________\n")
                    index = index +1
                    countVendasValor = countVendasValor = countVendasValor -1
                
                enter = input("\nAperte Enter para voltar")
                menuRelatorio = 0


            if int(menuRelatorio) == 3: #Valor total vendido
                clear()
                print("O total vendido em reais equivale a: R$",totalTotal)
                enter = input("\nAperte Enter para voltar")
                menuRelatorio = 0

            if int(menuRelatorio) == 4:
                clear()
                break

    elif menuGeral == 4:
        print('Fim do programa')
        break
    
    else: 
        menuGeral = int(input('{}, digite a opção Valida: '.format(nomeCliente)))