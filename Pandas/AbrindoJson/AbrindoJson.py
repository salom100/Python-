import pandas as pd 

dados = pd.read_json('dados.json')

print(dados.to_string())