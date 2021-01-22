import pandas as pd

dados = pd.read_csv("dados.csv")


print("DADOS SUJOS")
print(dados)

'''
#retorna um dataframe sem celulas vazias  (cria um novo data frame que é inserido na variavel limpando)
limpando = dados.dropna()
print("NOVO DATA FRAME SEM CELULAS VAZIAS")
print(limpando.to_string())
'''

'''
print("DATAFRAME ORIGINAL MODIFICADO PARA RETIRAR OS NULL")
#dados.dropna(inplace= True) altera os valores do dataFrame original
dados.dropna(inplace= True)
print(dados.to_string())
'''

'''
print("DATAFRAME ORIGINAL QUE PREENCHE 130 NOS NULL")
dados.fillna(130, inplace = True)
print(dados.to_string())
'''

'''
#Preenche na coluna calories os valores nulos por 130
dados["Calories"].fillna(130, inplace = True)
print(dados)
'''

'''
#Calculando a media e preenchendo a media nos valores nulos
x = dados["Calories"].mean()
dados["Calories"].fillna(x, inplace = True)
print("Media:",x)
print(dados.to_string())
'''

'''
#Calculando a mediana e preenchendo nos valores nulos
mediana= dados["Calories"].median()
dados["Calories"].fillna(mediana,inplace = True)
print("Mediana:",mediana)
print(dados.to_string())
'''

#calculando a moda e preenchendo no valores nulos 
moda = dados["Calories"].mode()[0]
dados["Calories"].fillna(moda, inplace = True)
print("MODA: ",moda)
print(dados.to_string())

