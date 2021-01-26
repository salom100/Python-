# Distribuição de poisson
'''
    distribuição do tipo discreta

    Estima quantas vezes um evento pode acontecer em um determinado momento


    lam = taxas ou numero conhecido de ocorrencias
    size = a forma da matriz retornada
'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


resultado = random.poisson(lam=2, size=10)
print(resultado)


sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#DIFERENÇA DE DISTRIBUIÇÃO NORMAL E DE POISSON
    # Normal = é de forma continua
    # Poisson = é discreta

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='Normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='Poisson')
plt.show()


''' DIFERENÇA ENTRE DISTRIBUIÇÂO DE POISSON E BINOMIAL
    Binomial= para tentativas discretas
    Poisson= para tentativas continuas

    n*p quase igual a lam
'''

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='Binomial')
sns.distplot(random.poisson(lam=10, size=1000),hist=False, label='Poisson')
plt.show()





