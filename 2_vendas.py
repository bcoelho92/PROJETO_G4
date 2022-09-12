# 2 - Vendas - Responsáveis Fernando e Thiago.

# (NOTA: As variáveis a seguir são só de exemplo para testar, vou alterar depois!)

from string import octdigits


produtos = {"arroz": 5, "feijão": 5, "macarrão": 10}        #Produtos listados e seu preço.
qtdProdutos = len(produtos)                                 #Quantidade de produtos no dicionário.

index = 0    #Referência para saber qual é a posição da lista

#01 - LISTANDO PRODUTOS - OK
print("Veja a seguir nosso catálogo de produtos: \n")
while qtdProdutos > 0:    #Enquanto houver produtos a serem listados
    print(list(produtos)[index].title())
    print("Preço: R$",float(list(produtos.values())[index]))
    print("\n")
    index = index +1
    qtdProdutos = qtdProdutos -1


#02 - ADICIONANDO PRODUTOS AO CARRINHO
carrinho = {}
addCarrinho = 1

while addCarrinho == 1:

    escolha = input("Informe o produto que deseja adicionar ao carrinho: ")
    while str(escolha).lower() not in produtos:    #Enquanto o nome digitado não estiver presente na lista de produtos.
                        # SÓ USAR LOWER SE FOR TUDO LOWER NOS PRODUTOS
        print("\nProduto inválido.")
        escolha = input("Informe um nome válido: ")
    #Produto escolhido definido.


    qtdEscolha = (input("Informe a quantidade desejada: "))

    while str(qtdEscolha).isnumeric() is not True or int(qtdEscolha) < 1:    #Enquanto a quantidade não for um número válido (int).
        print("\nQuantidade inválida.")
        qtdEscolha = (input("Informe uma quantidade válida: "))
    qtdEscolha = int(qtdEscolha)
    #Quantidade escolhida definida.

    carrinho[escolha] = qtdEscolha    #Adiciona ao carrinho

    questaoCarrinho = input("\nDeseja adicionar mais produtos ao carrinho? Digite SIM ou NÃO: ")
    while questaoCarrinho.lower() != "sim" and questaoCarrinho.lower() != "não":
        print("\nResposta inválida.")
        questaoCarrinho = input("Digite SIM ou NÃO: ")
    print("\n")

    if questaoCarrinho.lower() == "sim":
        addCarrinho = 1
    elif questaoCarrinho.lower() == "não":
        addCarrinho = 0


#03 - FINALIZAR COMPRA
print("Resumo da compra:")

countCarrinho = len(carrinho)
index = 0
total = 0

while countCarrinho > 0:
    print("\n")
    print((list(carrinho)[index]).title())
    print("Quantidade:", list(carrinho.values())[index])
    print("Preço:", produtos[list(carrinho)[index]])
    countCarrinho = countCarrinho -1
    total = total + produtos[list(carrinho)[index]]
    index = index +1

print("\n Total a pagar: ", total)
    
    