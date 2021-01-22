import pandas as pd
import matplotlib.pyplot as plt  

    
dados = pd.read_csv("dados.csv")

# GRAFICO DE LINHA
dados.plot()


#GRAFICOS DE PONTOS
dados.plot(kind='scatter', x='Duration', y='Calories')



#Grafico de dispersão aonde nao há relação entre as colunas
dados.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

#HISTOGRAMA
#ele so precisa de uma coluna
dados["Duration"].plot(kind="hist")

plt.show()