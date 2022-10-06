    #Sub-menu de Cadastro:
    #Cadastramento de produtos
    #Listar produtos cadastrados
    #Deleção de produtos 

from fileinput import filename
from flask import Flask 
from flask import render_template
from flask import url_for, redirect
from flask import request  
import numpy as np
import pandas as pd
import os

estoque = pd.read_csv('past_cadastro\estoque.csv') # Carrega o estoque 


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

menu=0
produto=[]
valor=[]
op="s"
# logica 

clear_console()
while op == "s":
    print(estoque)
    print()
    print("Vamos adicionar novos items ao cadastro !")
    produto.append(input("\nDigite o nome do produto: "))
    valor.append(input("\nDigite o valor do produto: R$ "))
    op = str(input("Deseja continudar: s/n "))
    clear_console() 

produto = pd.Series(produto,name='Produto')
valor = pd.Series(valor,name='Valor R$')

# salva o novo dicionario com as atualizações 
estoque1 = pd.DataFrame({
    'Produto':produto,
    'Valor':valor,
}) 

estoque.update(estoque1) #substitui os elementos começando com o zero do index
# estoque.copy(estoque1) #atualiza o estoque anterior com os novos itens 

print(f'''Estoque final: 
{estoque}''') # mostra o estoque atualizado

# estoque.to_csv('test dev/estoque.csv', index=False) #Salva dataframe novo



