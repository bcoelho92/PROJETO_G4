# 3 - Relatório - responsável Fernando
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


menuFernando = 3 #ISSO COMEÇA A RODAR MEU CÓDIGO
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


while menuFernando == 3:

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
        print(''' \n
******************************************
MENU VENDAS 

Essas são as opções do programa:  

[1] - Quantidade vendida por produto
[2] - Total vendido por produto (em reais)
[3] - Total vendido (em reais)
[4] - Voltar ao menu anterior

******************************************''')

        menuRelatorio = input("Digite a opção desejada: ")
        while str(menuRelatorio) not in "1234" or str(menuRelatorio).isnumeric() != True:#check
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
        menuFernando = 0
        menuGeral = ?? #SAIR DO MEU PROGRAMA