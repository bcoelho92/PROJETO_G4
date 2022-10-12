from flask import Flask
from flask import request
import pandas as pd

produtos=[]
valores=[]
quantidades=[]

app = Flask(__name__)
 
# logica 

@app.route('/')
def index():
    return "Hello!"

@app.route('/cadastrar')
def cadastro():
    argumentos = request.args.to_dict()
    produto1 = argumentos['produto']
    preco1 = argumentos['valor']
    quantidade1 = argumentos['quantidade']
    
    produtos.append(produto1)
    valores.append(preco1)
    quantidades.append(quantidade1)

estoque = pd.DataFrame(data={
    'Produtos':produtos,
    'Valores R$':valores,
    'Quantidade':quantidades
}).set_index('Produtos')

estoque.to_csv('past_cadastro/estoque.csv', index=False) #Salva dataframe

@app.route('/dataframe')

def dataframe():
    print(estoque)
    estoque.to_html('past_cadastro/estoque.html')
    return 'verifique no terminal'

if __name__ == "__main__":
    app.run(debug=True)