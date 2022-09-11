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


print("Você está no Menu de Cadastro de Produto! Digite Q para voltar ao menu anterior \n")

lista = {} #criando lista vazia 
qtd = int(input("Quantos produtos você gostaria de adicionar? ")) 

for i in range(qtd):
    produto = input("Digite o nome do produto: ")
    valor = input("Digite o valor do produto: ")
    lista[produto] = valor

clear_console()    
print("Produtos cadastrados:")
for produto in lista:
    print("-", (produto), "R$",(valor))

#remover item cadastrado
deleta = input("Qual produto você gostaria de deletar? Aperte ENTER para reexibir a lista: ")
if deleta in lista:
    lista.pop(deleta)
    print ("\nVocê apagou o item: \n-", (deleta), "\n")
    print("\nLista Atualizada:")
    print(lista)

elif deleta == "":
    print(lista)

else: print("\nProduto nao cadastrado!")



