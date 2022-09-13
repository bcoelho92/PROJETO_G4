# Será desenvolvido em conjunto de acordo com os resutados.
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


menuGeral = 3
menuRelatorio = 0
while menuGeral == 3:

    if menuRelatorio == 0:
        clear()
        print('''\n
    MENU DO RELATÓRIO

    1 - Quantidade vendida por produto
    2 - Valor vendido por produto
    3 - Total vendido (em dinheiro)
    4 - Voltar ao início
    ''')

        menuRelatorio = input("Digite a opção desejada: ")
        while str(menuRelatorio) not in "1234" or str(menuRelatorio).isnumeric() != True:#check
            print("\nOpção inválida")
            menuRelatorio = input("Digite uma opção válida: ")

    if menuRelatorio == 1:
        