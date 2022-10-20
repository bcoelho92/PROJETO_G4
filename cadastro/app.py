
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
    print(df)
    return 'Vide console por enquanto'

if __name__ == "__main__":
    app.run(debug=True)
