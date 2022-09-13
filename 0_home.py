# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Menu será elaborado no dia 09/09 
# 1 - Cadastro - Julia - Bruno (2)
# 2 - Vendas - Fernando - Tiago (2)
# 3 - Relatorio - relatorio sera desenvolvido de acordo com as entregas.

####################################################################################

# Boas vindas / 0 - Menu

import sys

# VARIAVEIS 

menu = 0
menu1 = 0
menu2 = 0
menu3 = 0

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

MENU VENDAS 

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

[1]-  Adição de produtos ao carrinho
[2] - Finalização da venda do carrinho
[3] - Voltar ao menu anterior
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

print()

# LÓGICA

nomeCliente = str(input('Digite sue nome: '))
print()
print ('Bem vindo(a) {} ao sistema de vendas da Organico’s!'.format(nomeCliente))

def main():
    while True:
        print(descm0.format(nomeCliente))
        menu = int(input('{}, digite a opção: '.format(nomeCliente)))
        print()
        if menu == 1:
            print (descm1)
            print()
            menu1 = int(input('{}, digite a opção [Menu cadastro]: '.format(nomeCliente)))
            print()
            while True:
                if menu1 == 1:
                    print ('funcao 1')
                elif menu1 == 2:
                    print('funcao 2')
                elif menu1 == 3:
                    print('funcao 3')
                elif menu1 == 4:
                    break
                elif menu1 == 5:
                    print ('Fim do programa')
                    sys.exit() 
                else: 
                    print('Opção invalida, digite uma opção valida: ')
        elif menu == 2:
            print (descm2)
            print()
            while True:
                print()
                menu2 = int(input('{}, digite a opção [Menu vendas]: '.format(nomeCliente)))
                print ()
                if menu2 ==1:
                    print('Adição de produtos ao carrinho')

                elif menu2 == 2:
                    print ('Finalização da venda do carrinho')

                elif menu2 == 3:
                    break
                elif menu2 == 4:
                    print ('Fim do programa')
                    sys.exit() 
                else: 
                    print('Opção invalida, digite uma opção valida: ')
        elif menu == 3:
            print (descm3)
            print()
            while True :
                menu3 = int(input('{}, digite a opção [Menu relatorio] : '.format(nomeCliente)))
                print()
                if menu3 ==1:
                    print('Funcao 1')
                elif menu3 == 2:
                    break
                elif menu3 == 3:
                    print ('Fim do programa')
                    sys.exit()
                else: 
                    print('Opção invalida, digite uma opção valida: ')          
        elif menu == 4:
            print('fim do programa')
            print()
            sys.exit
        else: 
            print('Opção invalida, digite uma opção valida: ')
            main()
main() 
