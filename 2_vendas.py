qtdEscolha = (input("Insira a quantidade desejada: "))


while str(qtdEscolha).isnumeric() is not True:
    print("Quantidade inválida.")
    qtdEscolha = int(input("\nInsira uma quantidade válida: "))

while qtdEscolha < 0:
    print("Quantidade inválida.")
    qtdEscolha = int(input("Insira uma quantidade válida: "))
    
    # 2 - Vendas - Responsáveis Fernando e Thiago.

# (NOTA: As variáveis a seguir são só de exemplo para testar, vou alterar depois!)

produtos = {"arroz": 5, "feijão": 5, "macarrão": 10}        #Produtos listados e seu preço.
qtdProdutos = len(produtos)                                 #Quantidade de produtos no dicionário


index = 0    #Referência para saber qual é a posição da lista

#01 - LISTANDO PRODUTOS
print("Veja a seguir nosso catálogo de produtos: \n")
while qtdProdutos > 0:   #Enquanto houver produtos a serem listados
    print(list(produtos)[index].title())
    print("Preço: R$",float(list(produtos.values())[index]))
    print("\n")
    index = index +1
    qtdProdutos = qtdProdutos -1


#02 - ADICIONANDO PRODUTOS AO CARRINHO
escolha = input(print("\nInsira o nome do produto que deseja adicionar ao carrinho: ")).title()
while escolha not in produtos:
    print("\nProduto inválido.")
    esolha = input(print("Insira um nome válido: ")).title()



qtdEscolha = (input("Insira a quantidade desejada: "))


while str(qtdEscolha).isnumeric() is not True:
    print("Quantidade inválida.")
    qtdEscolha = (input("Insira uma quantidade válida: "))

qtdEscolha = int(qtdEscolha).round()    #Para não ter números quebrados.

while qtdEscolha < 0:
    print("Quantidade inválida.")
    qtdEscolha = int(input("Insira uma quantidade válida: "))

# arredondar