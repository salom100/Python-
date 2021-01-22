import pandas as pd

dados = {
  "calorias": [420, 380, 390],
  "duração": [50, 40, 45]
}

# A série é como uma coluna, um DataFrame é a tabela inteira.
tabela = pd.DataFrame(dados)
print(tabela)
#print(tabela["calorias"])
#print(tabela["duração"])

# tabela.loc[linha] exibe todos os dados daquela linha
print(tabela.loc[1])

#É possivel selecionar mais de uma linha
# ao utilizar [] criamos um DataFrame pandas para exibir de melhor forma
print(tabela.loc[[0,1]])

#rotulando o dataFrame
rotulos = pd.DataFrame(dados, index = ["Dia1","Dia2","Dia3"])
print(rotulos)
#usando loc com rotulos
print(rotulos.loc["Dia2"])