# 3 - Relatório - responsável Fernando
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


menuFernando = 3
menuRelatorio = 0
carrinho = {"arroz": 2, "feijão": 3} #EXEMPLO
produtos = {"arroz": 5.0,"feijão": 7.0} #EXEMPLO

vendasValor = produtos #lista com o produto e seu preço (na lista de produtos)

#Adicionando todos os produtos da lista à lista quantidade vendidas:
#COLOCAR NO MENU DE CADASTRAMENTO
indexVendas = 0
countProdutos = len(produtos)
vendasQuant = {}
while countProdutos > 0:
    nomeProd = list(produtos)[indexVendas]
    vendasQuant[nomeProd] = 0
    indexVendas = indexVendas +1
    countProdutos = countProdutos -1#>


while menuFernando == 3:

    #CHECK - OPÇÃO 1 - Somando itens do carrinho ao relatório de vendas (sem prints)
    count = len(carrinho)
    indexSoma = 0
    while count > 0:
        nomeProd = list(carrinho)[indexSoma]
        quantProduto1 = carrinho[nomeProd]
        quantProduto2 = vendasQuant[nomeProd]
        novaQuant = quantProduto1 + quantProduto2
        vendasQuant[nomeProd] = novaQuant
        indexSoma = indexSoma+1
        count = count-1
        carrinho[nomeProd] = 0

    #CHECK - OPÇÃO 2 - Referenciar o dicionário de produtos.
    index = 0
    countVendasValor = len(produtos)
    totalTotal = 0
    while countVendasValor > 0:
        nomeProdutoVendido = (list(produtos)[index])
        quantProdutoVendido = vendasQuant[nomeProdutoVendido]
        precoProdutoVendido = produtos[nomeProdutoVendido]
        totalProdutoVendido = (int(quantProdutoVendido)*float(precoProdutoVendido))
        totalTotal = totalTotal +totalProdutoVendido
        index = index +1
        countVendasValor = countVendasValor = countVendasValor -1


    


    if int(menuRelatorio) == 0:
        clear()
        print('''\n
    MENU DO RELATÓRIO

    1 - Quantidade vendida por produto
    2 - Total vendido por produto (em reais)
    3 - Total vendido (em reais)
    4 - Voltar ao início
    ''')

        menuRelatorio = input("Digite a opção desejada: ")
        while str(menuRelatorio) not in "1234" or str(menuRelatorio).isnumeric() != True:#check
            print("\nOpção inválida")
            menuRelatorio = input("Digite uma opção válida: ")

    if int(menuRelatorio) == 4:
        menuFernando = 0


    if int(menuRelatorio) == 1: #Quantidade vendida de cada produto.
        clear()
        count = len(carrinho)
        indexSoma = 0
        while count > 0: #Somando itens do carrinho ao relatório de vendas
            nomeProd = list(carrinho)[indexSoma]
            quantProduto1 = carrinho[nomeProd] #Quantidade no carrinho
            quantProduto2 = vendasQuant[nomeProd] #Quantidade na lista de vendas
            novaQuant = quantProduto1 + quantProduto2
            vendasQuant[nomeProd] = novaQuant

            indexSoma = indexSoma+1
            count = count-1

            print(nomeProd.title())
            print("Quantidade vendida: ",novaQuant)
            print("\n")

            carrinho[nomeProd] = 0

        enter = input("Aperte Enter para voltar")
        menuRelatorio = 0
            


    if int(menuRelatorio) == 2: #Valor vendido de cada produto.
        clear()
        index = 0
        countVendasValor = len(produtos) #Referenciar o dicionário de produtos.
        totalTotal = 0
        while countVendasValor > 0:
            print((list(produtos)[index]).title())
            print("Preço por unidade: R$",list(produtos.values())[index])
            nomeProdutoVendido = (list(produtos)[index])
            quantProdutoVendido = vendasQuant[nomeProdutoVendido]
            precoProdutoVendido = produtos[nomeProdutoVendido]
            totalProdutoVendido = (int(quantProdutoVendido)*float(precoProdutoVendido))
            totalTotal = totalTotal +totalProdutoVendido
            print("Total vendido: R$",totalProdutoVendido)
            print("\n")
            index = index +1
            countVendasValor = countVendasValor = countVendasValor -1
        
        enter = input("\nAperte Enter para voltar")
        menuRelatorio = 0


    if int(menuRelatorio) == 3: #Valor total vendido
        clear()
        print("O total vendido em reais equivale a: R$",totalTotal)
        enter = input("\nAperte Enter para voltar")
        menuRelatorio = 0