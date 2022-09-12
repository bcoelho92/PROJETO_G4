# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Menu será elaborado no dia 09/09 
# 1 - Cadastro - Julia - Bruno (2)
# 2 - Vendas - Fernando - Tiago (2)
# 3 - Relatorio - relatorio sera desenvolvido de acordo com as entregas.

####################################################################################

# Boas vindas / 0 - Menu

''''''
print()
nomeCliente = str(input('Digite sue nome: '))
Menu = 0

print('''
***********************************************************
 Bem vindo(a) {} ao sistema de vendas da Organico’s! 
                                                     
 Essas são as opções do programa:           
                                                     
 [1] - Cadastro                                 
 [2] - Vendas                                   
 [3] - Relatório                                
 [4] - Sair                                     '
                                                     
***********************************************************
'''.format(nomeCliente))
    
def main():
    while True:
        menu = int(input('{}, digite a opção: '.format(nomeCliente)))
        print()
        
        if menu == 1:
            print ('Menu Cadastro')

            #   1 - Menu de Cadastro - Julia 
            #   Cadastramento de produtos
            #   *Listar produtos cadastrados*
            #   Deleção de produtos

        elif menu == 2:
            print ('Menu Vendas')

            #   2 - Menu de Vendas - Fernando 
            #   Adição de produtos ao carrinho
            #   Finalização da venda do carrinho (dizendo quanto o usuário tem que pagar)

        elif menu == 3:
            print ('Menu Relatorio ')

            #   3 - Menu Relatorio 
            #   Extrato de produtos vendidos

        elif menu == 4:
            print('fim do programa')
            break

        else: 
            print('Digite a opção valida: ')
            main()
            # 4 - Sair 

main() 