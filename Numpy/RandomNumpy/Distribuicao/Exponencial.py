#DISTRIBUIÇÂO EXPONENCIAL
'''
    Usada para descrever o tempo ate o proximo evento

    constituido por 2 parametros:
    scale= inverso da taxa padroniza para 1.0
    size= forma da matriz retornada    
'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

matriz= random.exponential(scale=2, size=(2,3))
print(matriz)

#Visualizando a distribuição
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

'''Relação entre Poisson e distribuição exponencial
A distribuição de Poisson lida com o número de ocorrências de um evento em um período de tempo, 
enquanto a distribuição exponencial lida com o tempo entre esses eventos.
'''