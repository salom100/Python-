import pandas as pd 

dados = pd.read_csv("dados.csv")
print("HEAD(5)")
#imprime as primeiras linhas
print(dados.head(5))
print("TAIL(5)")
#imprime as ultimas linhas
print(dados.tail(5))

#imprime informações dos dados
print(dados.info())