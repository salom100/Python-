import pandas as pd
'''
    Uma série Pandas é como uma coluna em uma mesa.
    É uma matriz unidimensional contendo dados de qualquer tipo.
'''
a = [2,4,6]

serie = pd.Series(a)
print("SERIES SEM ETIQUETA")
print(serie)
print(serie[2])

#Criando etiqueras
etiquetas = pd.Series(a, index= ["X","Y","Z"])
print("SERIES COM ETIQUETA")
print(etiquetas)
print("Valor do indice Y = ",etiquetas["Y"])