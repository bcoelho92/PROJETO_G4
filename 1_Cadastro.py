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

print (''' 

Bem vindo(a) ao Menu de Estoque! Digite a opção que você deseja:

1 - Cadastrar um novo produto
2 - Listar todos os Produtos Cadastrados 
3 - Apagar um Produto do Cadastro
4 - Sair
''')
print('')

# variaveis 

menu = int(input('Digite a opção desejada: '))

while menu >=5 or menu <=0:
    menu = int(input('Digite a opção válida: '))

if menu == 1:
    clear_console()
    print("Você deseja cadastrar um produto no estoque? Para retroceder, digite Q \n")

elif menu == 2:
    clear_console()
    print("Esses são os produtos cadastrados no estoque:")

elif menu == 3:
    clear_console()
    print("Você deseja apagar um produto do estoque? Para retroceder, digite Q \n")

elif menu == 4:
    clear_console()
    print("Saindo do Menu de Cadastro\n")


lista = {} #criando lista vazia 
qtd = int(input("\nQuantos produtos você gostaria de adicionar? ")) 

for i in range(qtd):
    produto = input("Digite o nome do produto: ")
    valor = input("Digite o valor do produto: ")
    lista[produto] = valor

clear_console()    
print("Produtos cadastrados:")
for produto in lista:
    print("-", (produto), "R$",(valor))

#remover item cadastrado
deleta = input("Qual produto você gostaria de deletar? Digite ENTER para reexibir a lista: ")
if deleta in lista:
    lista.pop(deleta)
    print ("\nVocê apagou o item: \n-", (deleta), "\n")
    print("\nLista Atualizada:")
    print(lista)

elif deleta == "":
    print(lista)

else: print("\nProduto nao cadastrado!")



