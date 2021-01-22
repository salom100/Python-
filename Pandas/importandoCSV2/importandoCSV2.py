import pandas as pd

dados = pd.read_csv("dados.csv")
#Por padrão, ao imprimir um DataFrame, você obterá apenas as 5 primeiras linhas e as 5 últimas linhas:
print(dados)

#imprime todo o dataFrame
print(dados.to_string())