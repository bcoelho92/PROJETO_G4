# Faremos o desenvolvmento em duplas, e cada dupla tera um arquivo de acordo com a distribuição.

# 0 - Menu - Menu será elaborado no dia 09/09 
# 1 - Cadastro - Julia - Bruno (2)
# 2 - Vendas - Fernando - Tiago (2)
# 3 - Relatorio - relatorio sera desenvolvido de acordo com as entregas.

####################################################################################

# Boas vindas / 0 - Menu

nomeCliente = str(input('Digite sue nome: '))
print('')
print('''
|*****************************************************|
| Bem vindo(a) {} ao sistema de vendas da Organico’s! |
|                                                     |
| Digute o numero da opção que você deseja:           |
|                                                     |
| Digite 1 - Cadastro                                 |
| Digute 2 - Vendas                                   |
| Digute 3 - Relatório                                |
| Digute 2 - Sair                                     |
|                                                     |
*******************************************************
'''.format(nomeCliente))

menu = int(input('Digite a opção do Menu: '))

print('')

menu = int(input('Digite a opção desejada: '))
import os

while menu >=5 or menu <=0:
    menu = int(input('Digite a opção valida: '))
    os.system('clear')
       
if menu == 1:
    n1 = float(input('digite primeiro numero: '))
    n2 = float(input('digite segundo numero: '))
    r = n1+n2
    print ('A somea de {} e {} é igaul {}'.format(n1,n2,r))

elif menu == 2:
        print("vamos Subtrair")
        n1 = float(input('digite primeiro numero: '))
        n2 = float(input('digite segundo numero: '))
        r = n1-n2
        print ('A Subtração de {} e {} é igaul {}'.format(n1,n2,r))


elif menu == 3:
        print('Seu Dividir!')
        n1 = float(input('digite primeiro numero: '))
        n2 = float(input('digite segundo numero: '))
        r = n1*n2
        print ('A multi de {} e {} é igaul {}'.format(n1,n2,r))

elif menu == 4:
        print('Sair, grato pelo seu acesso!')

#-----

print('')
print('fim do programa!')





# Variaveis 


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
