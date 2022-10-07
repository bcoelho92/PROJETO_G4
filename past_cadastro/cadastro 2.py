from flask import Flask
from flask import request
import pandas as pd

app = Flask(__name__)

produtos = {} # {produto: [valor, quantidade]}

@app.route('/')
def index():
    return "Hello!"

@app.route('/cadastrar') 
def cadastro():
    argumento = request.args.to_dict()

    produto = argumento['produto']
    preco = argumento['preco']
    quantidade = argumento['quantidade']

    #dicionario
    produtos[produto] = [preco, quantidade]

    produtos.to_csv('past_cadastro/estoque.csv', index=False) #Salva dataframe
    return 'Produtos foram cadastrados'


@app.route('/dicionario')
def dicionario():
    return produtos #fernando

@app.route('/dataframe')
def dataframe():
    print(produtos)
    return 'verifique no terminal'

if __name__ == "__main__":
    app.run(debug=True)