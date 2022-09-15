# 1 - Cadastro - responsaveis Julia e Bruno (2)
    #Sub-menu de Cadastro:
    #Cadastramento de produtos
    #Listar produtos cadastrados
    #Deleção de produtos 
    
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
clear_console() 

menu=0
while menu !=6:

    print (''' 
    ******************************************
    MENU CADASTRO 

    Essas são as opções do programa:  

    [1] - Cadastramento de produtos
    [2] - Listar produtos cadastrados
    [3] - Deleção de produtos
    [4] - Voltar ao menu anterior
    [5] - Sair    

    ******************************************
    ''')
    print('')


    menu = int(input('Digite a opção desejada: '))

    while menu >=6 or menu <=0:
        menu = int(input('Digite uma opção válida: '))

    if menu == 1:
        clear_console()

        # lista = {} #criando lista vazia 
        # listaadd = {}
        
        # produto = input("Digite o nome do produto: \n").title()
        # valor = float(input('Insira o preço do produto a ser cadastrado\n'))

        # if produto in lista:
        #     lista[produto] = lista[produto] + valor
        # else:
        #     lista[produto] = valor

        # clear_console()
        # print("\n Você adicionou ao estoque:\n", lista, "\n")

        lista = {}
        listaadd = {}

        qtd = int(input("\nQuantos produtos você gostaria de cadastrar? ")) 

        for i in range(qtd):
            produto = input("Digite o nome do produto: ").title()
            valor = float(input("Digite o preço do produto: "))
            lista[produto] = valor
        
        print("\nVocê cadastrou esses itens:\n")
        print(lista)

        submenu = int(input("\nGostaria de acrescentar mais produtos? Digite 1 p/ sim ou 2 para voltar:\n"))
        if submenu == 1:
            clear_console()
            num = int(input("\nQuantos produtos você gostaria de cadastrar? ")) 
            for e in range(num):
                produtoadd = input("Digite o nome do produto: ").title()
                valoradd = float(input("Digite o preço do produto: "))

            listaadd[produtoadd] = valoradd
            lista.update(listaadd)
            print("\nLista Atualizada:\n ")
            print(lista)
            print('')

        if submenu == 2:
            clear_console()
            print('\nVoltando ao menu de cadastro:\n')
        while submenu >=3 or menu <=0:
            submenu = int(input('Digite uma opção válida: Digite 1 p/ cadastrar produto ou 2 para voltar: '))
        #else:
             #print('\nVoltando ao menu de cadastro:\n')

    elif menu == 2:
        clear_console()
        print("\nProdutos cadastrados no estoque:\n")
        for produto in lista:
            print("-", (produto), "R$",(valor))

    elif menu == 3:
        clear_console()
        print("Você deseja apagar um produto do estoque? Para retroceder, digite Q \n")
        #remover item cadastrado
        deleta = input("Qual produto você gostaria de deletar? Digite ENTER para reexibir a lista: ").title()
        if deleta in lista:
            lista.pop(deleta)
            print ("\nVocê apagou o item: \n-", (deleta), "\n")
            print("\nLista Atualizada:")
            print(lista)
        elif deleta == "":
            print(lista)
        else: print("\nProduto nao cadastrado!")

    elif menu == 4:
        clear_console()
        print("Saindo do Menu de Cadastro\n")

    elif menu == 5:
        clear_console()
        print("Fechando o Sistema\n")
        


    