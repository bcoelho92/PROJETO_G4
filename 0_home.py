# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Menu será elaborado no dia 09/09 
# 1 - Cadastro - Julia - Bruno (2)
# 2 - Vendas - Fernando - Tiago (2)
# 3 - Relatorio - relatorio sera desenvolvido de acordo com as entregas.

####################################################################################

# Boas vindas / 0 - Menu
print()
nomeCliente = str(input('Digite sue nome: '))

def main():
    while True:
        print('''
***********************************************************
 Bem vindo(a) {} ao sistema de vendas da Organico’s! 
                                                     
 Digute o numero da opção que você deseja:           
                                                     
 [1] - Cadastro                                 
 [2] - Vendas                                   
 [3] - Relatório                                
 [4] - Sair                                     
                                                     
***********************************************************
'''.format(nomeCliente))
    
        menu = int(input('Digite a opção: '))
        print()
        
        if menu == 1:
            print ('Cadastro')
        elif menu == 2:
            print ('Vendas')
        elif menu == 3:
            print ('Relatorio ')
        elif menu == 4:
            print('fim do programa')
            break
        else: 
            print('Digite a opção valida: ')
            main()
main() 


# 1 - Menu de Cadastro - Julia - Bruno (Steep 1 )

#   Cadastramento de produtos
#   *Listar produtos cadastrados*
#   Deleção de produtos

# 2 - Menu de Vendas - Fernando - Tiago (Steep 2)
#   Adição de produtos ao carrinho
#   Finalização da venda do carrinho (dizendo quanto o usuário tem que pagar)

# 3 - Relatorio ( steep 4 )
#   Extrato de produtos vendidos

# 4 - Sair (Steep 3 )

