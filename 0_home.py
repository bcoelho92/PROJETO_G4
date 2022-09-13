# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Bruno 
# 1 - Cadastro - Julia 
# 2 - Vendas - Fernando
# 3 - Relatorio - Fernando

####################################################################################

# Boas vindas / 0 - Menu

import sys
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# VARIAVEIS 

menuGeral = 0
menuCad = 0
menuVendas = 0
menuRelat = 0

descm0 ='''
******************************************
MENU PRINCIPAL

Essas são as opções do programa:           
                                                     
[1] - Cadastro                                 
[2] - Vendas                                   
[3] - Relatório                                
[4] - Sair                                     
                                                     
****************************************** '''
descm1 =''' 
******************************************
MENU CADASTRO 

Essas são as opções do programa:  

[1] - Cadastramento de produtos
[2] - Listar produtos cadastrados
[3] - Deleção de produtos
[4] - Voltar ao menu anterior
[5] - Sair    

******************************************'''
descm2 =''' 
******************************************
MENU VENDAS 

Essas são as opções do programa:  

[1] - Adição de produtos ao carrinho
[2] - Remover produtos ao carrinho
[3] - Finalização da venda do carrinho
[4] - Voltar ao menu anterior
[4] - Sair    

******************************************'''
descm3 =''' 
******************************************
MENU RELATÓRIO

Essas são as opções do programa:  

[1]-  Extrato de produtos vendidos
[2] - Voltar ao menu anterior
[3] - Sair    

******************************************'''

#vendas 

carrinho = {} #Definir essa variável no começo do programa
produtos = {"arroz": 6, "feijão": 8, "macarrão": 12, "sal": 2, "açúcar": 3} #Dicionário com todos os produtos
qtdProdutos = len(produtos)


print()

# LÓGICA

nomeCliente = str(input('Digite sue nome: '))
print()
print ('Bem vindo(a) {} ao sistema de vendas da Organico’s!'.format(nomeCliente))

def main():
    while True:
        print(descm0.format(nomeCliente))
        menuGeral = int(input('{}, digite a opção: '.format(nomeCliente)))
        print()
        if menuGeral == 1:
            print (descm1)
            print()
            menuCad = int(input('{}, digite a opção [Menu cadastro]: '.format(nomeCliente)))
            print()
            while True:
                if menuCad == 1:
                    print ('funcao 1')
                elif menuCad == 2:
                    print('funcao 2')
                elif menuCad == 3:
                    print('funcao 3')
                elif menuCad == 4:
                    break
                elif menuCad == 5:
                    print ('Fim do programa')
                    sys.exit() 
                else: 
                    print('Opção invalida, digite uma opção valida: ')
        elif menuGeral == 2:
            print (descm2)
            print()
            while True:
                print()
                menuVendas = int(input('{}, digite a opção [Menu vendas]: '.format(nomeCliente)))
                print ()
                if menuVendas ==1:
                    print('Adição de produtos ao carrinho')
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

                elif menuVendas == 2:
                    print ('Remnmover produtos do Carrinho. ')
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
                            enter = input("Aperte Enter para voltar ao início.")
                            menuVendas = 0
                    elif questaoRemover.lower() == "não":
                        menuVendas = 3   
                                         
                elif menuVendas == 3:
                    print ('Finalização da venda do carrinho')
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

                    print(descm2)
                    menuVendas = input("\nDigite a opção desejada: ")
                    if str(menuVendas) not in "1230":#check
                        print("Opção inválida!")
                        menuVendas = input("Digite novamente: ")

                    if int(menuVendas) == 3 and total_local != 0: #Finalizar compra
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
                        enter = input("\nAperte Enter para voltar ao menu inicial")
                        carrinho = {}
                        menuVendas = 0
                    
                    if total_local == 0:
                        print("\nSeu carrinho está vazio!")
                        enter = input("Aperte Enter para voltar")
                        menuVendas = 0
                elif menuVendas == 4:
                    break
                elif menuVendas == 5:
                    print ('Fim do programa')
                    sys.exit() 
                else: 
                    print('Opção invalida, digite uma opção valida: ')
                    
        elif menuGeral == 3:
            print (descm3)
            print()
            while True :
                menuRelat = int(input('{}, digite a opção [Menu relatorio] : '.format(nomeCliente)))
                print()
                if menuRelat ==1:
                    print('Funcao 1')
                elif menuRelat == 2:
                    break
                elif menuRelat == 3:
                    print ('Fim do programa')
                    sys.exit()
                else: 
                    print('Opção invalida, digite uma opção valida: ')          
        elif menuGeral == 4:
            print('fim do programa')
            print()
            sys.exit
        else: 
            print('Opção invalida, digite uma opção valida: ')
            main()
main() 
