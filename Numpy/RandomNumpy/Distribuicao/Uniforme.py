#Distribuição uniforme
'''
    descreve a probabilidade de eventos iguais acontecerem

    a= limite inferior
    b= limite superior
    size = matriz retornada

'''
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

matriz = random.uniform(size=(2,3))
print(matriz)

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()


