import pandas as pd

tabGeral = pd.read_csv("C:\\Users\\FE_GAVA\\Documents\\projetoMAGALU\\PROJETO_G4\\fe_csv_exemplo.csv")

#1. Quantidade vendida por produto.
produtosRel = tabGeral["Produto"]
produtosRel = produtosRel.tolist() #Nomes dos produtos.
SER_produtos = pd.Series(produtosRel, name='Produto', dtype=object) #>1

qtdVendida = tabGeral.iloc[:,4:].sum(axis=1)
qtdVendida = qtdVendida.tolist()  #Soma das quantidades vendidas.
SER_quantidade = pd.Series(qtdVendida, name="Unidades vendidas", dtype=object) #>3


#2. Valor vendido por produto.
precosRel = tabGeral["Preço"]
precosRel = precosRel.tolist() #Preço dos produtos.
SER_precos = pd.Series(precosRel, name="Preço", dtype=object) #>2

valorVendido = [a*b for a,b in zip(precosRel,qtdVendida)] #Valor vendido por produto.
SER_valor = pd.Series(valorVendido, name="Valor vendido", dtype=object) #>4

#3. Total vendido.
totalVendas = sum(valorVendido)

#Montando o DataFrame:
DF_relatorio = pd.DataFrame ({
    "Produto": SER_produtos,
    "Preço": SER_precos,
    "Unidades vendidas": SER_quantidade,
    "Valor vendido": SER_valor,
})
