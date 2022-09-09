# 1 - Cadastro - responsaveis Julia e Bruno (2)
# Rascunho de funções

#criar txt de produtos cadastrados
#como adicionar precificação?
#menu de cadastro de itens
    #def menu(produtos):
    #print( 'Você tem X itens na sua lista \nDigite 1 para exibir sua lista \nDigite 2 para adicionar um item da lista \nDigite 3 para remover um item da lista.')

#criar lista
produtos = []
print(f'Lista de produtos cadastrados: {produtos}')

# Usando append() pra adicionar novo item
f = input('Inclua um novo produto:\n')
produtos.append(f)

#Mostrar numero de itens na lista
print('Total de itens cadastrados ', len(produtos))

#imprimir lista
print(f'Lista de produtos atualizada: {produtos}')

#indexar cada item começando por 0 (ou usar enumerate()?)
for index in range(len(produtos)):
    print(index),produtos[index]

#remover um item da lista pelo número indexado
p = input('Digite o numero do produto que você quer remover:\n')
produtos.pop()
print(f'Lista de produtos atualizada: {produtos}')





