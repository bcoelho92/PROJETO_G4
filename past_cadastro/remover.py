from flask import render_template, redirect
from flask import Flask
from flask import request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('past_cadastro/estoque.csv')

@app.route('/')
def estoque():
    print(df)
    return 'veja o terminal'

@app.route('/deleta/<id>')
def deleta():
    mask_id = df[df['id'] == int(id)].index #mascara do ID
    df.drop(mask_id, axis=0, inplace=True)
    return redirect('/')


if __name__ == "__main__":
    app.run()