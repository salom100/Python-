import pandas as pd

calorias = {"day1": 420, "day2": 380, "day3": 390}


#Transformas as chaves do dicionario em rotulos correspondentes a cada numero
dados = pd.Series(calorias)
print(dados)

selecionados = pd.Series(calorias, index = ["day2","day3"])
print("dados selecionados:\n",selecionados)