# ***** ROTAS *****
# http://127.0.0.1:5000
# http://127.0.0.1:5000/cadastro
# http://127.0.0.1:5000/adicionar
# http://127.0.0.1:5000/deletar
# http://127.0.0.1:5000/estoque

# ***** FORMULARIOS *****
# http://127.0.0.1:5000/static/index.html
# http://127.0.0.1:5000/static/cadastrar.html
# http://127.0.0.1:5000/static/adicionar.html
# http://127.0.0.1:5000/static/deletar.html

from email import header
from fileinput import filename
from re import A
from flask import render_template, url_for , redirect # Ler aruivos HTML
from flask import request
import pandas as pd
from flask import Flask

app = Flask(__name__)

produtos_lista = []
precos = []
quantidades = []
produtos = {}
'''
df = pd.DataFrame(data={
        'Produto': [],
        'Preco': [],
        'Quantidade': []
    }).set_index('Produto')
'''
df = pd.read_csv('cadastro/estoque.csv',index_col='Produto') # ok

@app.route('/') # ok
def index():
    return redirect('http://127.0.0.1:5000/static/index.html')

@app.route('/cadastro') # ok 
def cadastro():
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']
    #listas
    produtos_lista.append(produto)
    precos.append(preco)
    quantidades.append(quantidade)
    #dicionario
    produtos[produto] = [preco, quantidade]
    #dataframe
    df.loc[produto] = [preco, quantidade]

    df.to_csv('cadastro/estoque.csv')
    return redirect('http://127.0.0.1:5000/static/back_home.html')

'''
@app.route("/adicionar") # ok
def adicionar():
    argumentos = request.args.to_dict()
    # Argumentos em listas  
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']

    df.loc[produto] = [preco, quantidade]
    
    df.to_csv('cadastro/estoque.csv') 
    return 'Prodtuto adicionado'
'''
@app.route("/deletar") # OK
def remover():
    global df
    argumentos = request.args.to_dict()
    # coletar argumento INDEX   
    deleta = argumentos['produto']
    deleta = str(deleta)
    # apaga o item do dataframe com base no digito do produto.
    df = df.drop(deleta, axis=0)
    # Salva dataframe em CSV
    df.to_csv('cadastro/estoque.csv') 
    print(df)
    return redirect('http://127.0.0.1:5000/static/back_del.html')
    
@app.route("/estoque") # pendnete 
def estoque():
    df = pd.read_csv('cadastro/estoque.csv',index_col='Produto')
    #print(df)
    #return 'Vide console por enquanto'
    df.to_html("cadastro/templates/Table.htm")
    html_file = df.to_html()
    return redirect('cadastro/templates/Table.htm')

''' 
VENDAS A IMPLANTAR 


RELATORIO A IMPLANTAR 

#<<Lógica:
tabGeral = pd.read_csv("cadastro\estoque.csv") #Arquivo CSV com tudo.
#1. Quantidade vendida por produto.
produtosRel = tabGeral["Produto"]
produtosRel = produtosRel.tolist() #Lista com nomes dos produtos.
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
#>>

#<<Pro HTML:
#Transformando o cabeçalho do DataFrame em uma lista.
li_cabecalho = list(DF_relatorio.columns.values)

#Transformando todos os dados em lista de tuplas.
li_data = list(DF_relatorio.itertuples(index=False, name=None))

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html", li_cabecalho=li_cabecalho, li_data=li_data, totalVendas=totalVendas)
    #Nos parâmetros segundo e teceiro, estamos criando uma variável que será lida pelo Jinja no arquivo HTML.
    #Igualando o nome das variáveis de lá e daqui, respectivamente.
#>>
'''
if __name__ == "__main__":
    app.run(debug=True)