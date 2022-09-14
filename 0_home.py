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

print()
print('******************************************************************************')
nomeCliente = str(input('Digite sue nome: '))

descm0 = '''
******************************************************************************
            Bem vindo(a) {} ao sistema de vendas da Organico’s!
******************************************************************************
MENU PRINCIPAL

Essas são as opções do programa:           
                                                     
[1] - Cadastro                                 
[2] - Vendas                                   
[3] - Relatório                                
[4] - Sair                                     
                                                     
*******************************************************************************'''
descm1 ='''
******************************************************************************
MENU CADASTRO 

Essas são as opções do programa:  

[1] - Cadastramento de produtos
[2] - Listar produtos cadastrados
[3] - Apagar um Produto do Cadastro
[4] - Voltar ao menu anterior
[5] - Sair    

******************************************************************************'''
descm2 =''' 
******************************************************************************
MENU VENDAS 

Essas são as opções do programa:  

[1] - Adição de produtos ao carrinho
[2] - Remover produtos ao carrinho
[3] - Finalização da venda do carrinho
[4] - Voltar ao menu anterior
[4] - Sair    

******************************************************************************'''
descm3 =''' 
******************************************************************************
MENU RELATÓRIO

Essas são as opções do programa:  

[1]-  Extrato de produtos vendidos
[2] - Voltar ao menu anterior
[3] - Sair    

******************************************************************************'''

#vendas 

carrinho = {} #Definir essa variável no começo do programa
produtos = {"arroz": 6, "feijão": 8, "macarrão": 12, "sal": 2, "açúcar": 3} #Dicionário com todos os produtos
qtdProdutos = len(produtos)


print()

# LÓGICA

def main():
    while True:
        print(descm0.format(nomeCliente))
        menuGeral = int(input('{}, digite a opção: '.format(nomeCliente)))
        print()
# Cadastro
        if menuGeral == 1:
#            def vend ():
            while True:
                print (descm1)
                print()
                menuCad = int(input('{}, digite a opção [Menu cadastro]: '.format(nomeCliente)))
                print()       
                
                if menuCad == 1:
                    clear()
                    print('*******************************************************************************')
                    print("Você deseja cadastrar um produto no estoque? Para retroceder, digite Q \n")
                    lista = {} #criando lista vazia 
                    qtd = int(input("\nQuantos produtos você gostaria de adicionar? ")) 

                    for i in range(qtd):
                        produto = input("Digite o nome do produto: ").title()
                        valor = input("Digite o valor do produto: ")
                        print('*******************************************************************************')
                        lista[produto] = valor

                elif menuCad == 2:
                            clear()
                            print("Esses são os produtos cadastrados no estoque:") 
                            print()
                            print("Produtos cadastrados:")
                            for produto in lista:
                                print()
                                print("-", (produto), "R$",(valor))
                                print('*******************************************************************************')
                        #    break  
                        # Ajustar back do menu  
                elif menuCad == 3:
                    clear()
                    print("Você deseja apagar um produto do estoque? Para retroceder, digite Q \n")
                    #remover item cadastrado
                    deleta = input("Qual produto você gostaria de deletar? Digite ENTER para reexibir a lista: ").title()

                    if deleta in lista:
                        lista.pop(deleta)
                        print ("\nVocê apagou o item: \n-", (deleta), "\n")
                        print("\nLista Atualizada:")
                        print(lista)
                        print('*******************************************************************************')
                    elif deleta == "":
                        print(lista)

                    else:print("\nProduto nao cadastrado!")
                    break
                elif menuCad == 4:
                    break
                elif menuCad == 5:
                    print('Fim do programa, {} obrigado e Até a proxima!'.format(nomeCliente))
                    print()
                    sys.exit(2)
                else: 
                    print('Opção invalida, digite uma opção valida: ')
# Vendas
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
                    
                elif menuVendas == 2:
                    print ('Remnmover produtos do Carrinho. ')
                    clear()
                                            
                elif menuVendas == 3:
                    print ('Finalização da venda do carrinho')
                    clear()
                  
                elif menuVendas == 4:
                    break
                elif menuVendas == 5:
                    print ('Fim do programa')
                    sys.exit() 
                else: 
                    print('Opção invalida, digite uma opção valida: ')   
# Relatorio               
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
# Sair        
        elif menuGeral == 4:
            print('Fim do programa, {} obrigado e Até a proxima!'.format(nomeCliente))
            print()
            break
            
        else: 
            print('Opção invalida, digite uma opção valida: ')
            main()
main() 
