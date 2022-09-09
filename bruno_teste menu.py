# teste menu 
import os
print (''' 

Digite a opão que vc deseja:

1 - Soma
2 - sub 
3 - relatorio
4 - Sair
''')
print('')

# variaveis 

menu = int(input('Digite a opção desejada: '))

while menu >=5 or menu <=0:
    menu = int(input('Digite a opção valida: '))
    os.system('clear')
       
if menu == 1:
        print (' Vamos Somar:')
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

print('')
print('fim do programa!')


    




