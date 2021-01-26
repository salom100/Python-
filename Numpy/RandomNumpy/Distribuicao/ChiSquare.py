#Distribuição Chi Square
'''
    usada como base para verificar a hipotese

    constituida por 2 parametros:
    df= grau de liberdade
    size = forma da matriz retornada
'''
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns


matriz = random.chisquare(df=2, size=(2,3))
print(matriz)

# visualização da distribuição
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

