from email import header
from fileinput import filename
from flask import render_template, url_for , redirect# Ler aruivos HTML
from flask import request
import pandas as pd
from flask import Flask


app = Flask(__name__)

produtos_lista = []
precos = []
quantidades = []
produtos = {} # {produto: [valor, quantidade]}

df = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')

'''
iloc # posição 0,1,2,3,4,5
loc # index arroz, feijao
'''
df = pd.read_csv('produtos.csv', index_col='produto')

print(df)
@app.route('/')
def index():
    return "Hello!"

@app.route('/cadastro') # /cadastro?produto=valor_produto&valor=valor_preco&quantidade=valor_quantidade
def cadastro():
    argumentos = request.args.to_dict()
    '''
    {
        'produto': valor_produto,
        'preco': valor_preco,
        'quantidade': valor_quantidade,
    }
    '''
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
    df.to_csv('produtos.csv')
    return 'Produtos foram cadastrados'

@app.route("/adicionaar")
def adicionar():
    # faz a leitura 
    df = pd.read_csv('produtos.csv', index_col='produto')
    argumentos = request.args.to_dict()
    # Argumentos em listas  
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']
    # transfor lt em df
    adicionar = pd.DataFrame(data={
        'Produtos':produto,
        'Valores R$':preco,
        'Quantidade':quantidade
    })
    # mnstra o df-adicionar
    print (adicionar)
    # adiciona mais uma linha no dataframe com base no df-adicionar
    df.loc[len(df)] = adicionar
    # Salva dataframe em CSV
    df.to_csv('/estoque.csv', index=False) 
    return 'Prodtuto adicionado'

@app.route("/deletar")
def remover():
    # monstrar data frame
    df = pd.read_csv('produtos.csv', index_col='produto')
    argumentos = request.args.to_dict()
    # coletar argumento INDEX   
    deleta = argumentos['produto']
    # apaga o item do dataframe com base no digito do produto.
    df.drop(deleta,axis=0, implace=True)
    # Salva dataframe em CSV
    df.to_csv('/estoque.csv', index=False) 
    print(df)
    return 'Produto deletado'
    
if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/cadastrar
# http://127.0.0.1:5000/adicionar
# http://127.0.0.1:5000/remover
# http://127.0.0.1:5000/produtos
