#Distribuição Logistica
'''
    Usada para descrever o crescimento
    usado em machine learning em regressão logistica, redes neurais

    constituido por:
    loc= aonde esta o pico (padrao 0)
    scale= desvio padrao, planura da distribuição (padrao 1)
    size= forma da matriz retornada

'''
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

matriz = random.logistic(loc=1, scale=2, size=(2,3))
print(matriz)

sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

#DISTRIBUIÇÂO LOGISTICA VS NORMAL
'''
    Quase identicas, porem a logistica tem mais area sob as caudas
    Representa mais ocorrencias que estejam distantes da media

    Para valores de escala mais altos (desvio padrão), 
        as distribuições normal e logística são quase idênticas, exceto pelo pico.
'''
sns.distplot(random.normal(scale=2, size=1000), hist=False, label="Normal")
sns.distplot(random.logistic(size=1000), hist=False, label="Logistica")
plt.show()

