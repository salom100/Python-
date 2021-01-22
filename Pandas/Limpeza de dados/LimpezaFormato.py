import pandas as pd

dados = pd.read_csv('dados.csv')
print(dados)

#formatando as datas para seguir um unico padrão
print("LIMPEZA DE FORMATO (DATETIME)")
#dados["coluna"] = pd.to_datetime(dados["coluna"])
dados["Date"] = pd.to_datetime(dados["Date"])
print(dados)

#Remova a linha que tiver valor null na coluna Date
dados.dropna(subset =["Date"], inplace = True)
print(dados)

#CORRIGINDO DADOS ERRADOS

#no dataFrame no index 7 da coluna Duration substituir o valor por 45
dados.loc[7,'Duration'] = 45
print(dados)

#looping nos valores de uma coluna
for i in dados.index:
    if dados.loc[i, "Duration"] > 120:

        #Substituimos o valor por 120
        dados.loc[i,"Duration"] = 120

        #ou excluimos a linha
        #dados.drop[i, inplace = True]

print(dados)

# Descobrindo valores duplicados
#dados.duplicated() retorna True os valores que sao duplicados, caso contrario retorna False
print(dados.duplicated())

#Removendo dados duplicados
#inplace remove do dataFrame original
dados.drop_duplicates(inplace = True)
print(dados)

