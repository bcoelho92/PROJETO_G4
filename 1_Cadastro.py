# 1 - Cadastro - responsaveis Julia e Bruno (2)
# Rascunho dicionario

lista = {} #criando lista vazia p/ cadastro de produtos

#input p/ definir quantidade de itens para acrescentar
qtd = int (input('Quantos produtos você gostaria de adicionar? ')) 

for i in range(qtd):
    produto = input('Digite o nome do produto: ')
    valor = input('Digite o valor do produto: ')
    lista[produto] = valor

print(lista)