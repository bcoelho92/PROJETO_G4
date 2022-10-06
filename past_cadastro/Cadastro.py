# 1 - Cadastro - responsaveis Julia e Bruno (2)
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
    print("Vamos cadastra !\n")
    produto.append(input("\nDigite o nome do produto: "))
    valor.append(input("\nDigite o valor do produto: R$ "))
    op = str(input("Deseja continudar: s/n "))
    clear_console() 

produto = pd.Series(produto,name='Produto')
valor = pd.Series(valor,name='Valor R$')

estoque = pd.DataFrame({
    'Produto':produto,
    'Valor':valor,
})

print(f'''Estoque final: 
{estoque}''')

estoque.to_csv('test dev/estoque.csv', index=False) #Salva dataframe



