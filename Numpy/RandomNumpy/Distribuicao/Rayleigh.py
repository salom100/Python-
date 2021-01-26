#Distribuição de Rayleigh
'''
    é usada no processamento de sinais

    parametros:
    scale= (desvio padrao) decide o quao plana a distribuição sera o padrao 1.0
    size= forma da matriz retornada
'''

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

matriz= random.rayleigh(scale=2, size=(2,3))
print(matriz)

#Visualização da distribuição
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

#SIMILITUDES ENTRE CHI SQUARE E RAYLEIGH
'''
    o e 2 graus de liberdade rayleigh e qui quadrado representam as mesmas distribuições
'''