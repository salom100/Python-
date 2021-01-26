#Distribuição de Pareto
'''
    seguindo a lei de pareto 80-20(fatores de 20% causa resultado de 80%)

    Parametros:
    a= parametro de forma
    size= a forma da matriz retornada
'''
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

matriz = random.pareto(a=2, size=(2,3))
print(matriz)

#Visualizando 
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()