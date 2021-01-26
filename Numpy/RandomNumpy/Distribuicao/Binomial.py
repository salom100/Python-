#Distribuição Binomial
'''é uma distribuição discreta
    constituida de 3 parametros
    n = numero de tentativas
    p = probabilidade da ocorrencia de cada alternativa
    size = a forma da matriz que queremos

    Diferença entre normal e binomial
        a distribuição normal e continua e a binomial é discreta

'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

resultado = random.binomial(n=10, p=0.5, size= 10)

print(resultado)

sns.distplot(random.binomial(n=10, p=0.5, size= 1000), hist= True, kde= False)
plt.show()

sns.distplot(random.normal(loc=50, scale= 2, size= 1000 ), hist=False, label='Normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='Binomial')
plt.show()