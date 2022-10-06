# Deleção de produtos 

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

estoque = pd.read_csv('past_cadastro\estoque.csv') # Carrega o estoque 
menu=0
op="s"
deleta=[]

# logica 

clear_console()

while op == "s":
    print("Vamos Deleção de produtos !\n")
    print(estoque)
    deleta = str(input("\nQual item deseja deletar ? ")) 
    
    
    [estoque.pop(key) for key in [deleta]]

    print(estoque)

    op = str(input("Deseja continudar: s/n "))
    clear_console() 

print(f'''Estoque final: 
{estoque}''')

# estoque.to_csv('test dev/estoque.csv', index=False) #Salva dataframe



