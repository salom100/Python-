# Distribuição de Zipf
'''
    Exibe os dados seguindo a lei de Zipf

Lei de Zipf
    Em uma coleção, o enésimo termo comum é 1 / n vezes do termo mais comum. 
    Por exemplo, a 5ª palavra comum em inglês ocorre quase 1/5 vezes a partir da palavra mais usada.

    Parametros:
    a= parametro da distribuição
    size= matriz retornada
'''

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

matriz = random.zipf(a=2, size=(2,3))

print(matriz)

#Visualizando
matriz = random.zipf(a=2, size=1000)
sns.distplot(matriz[matriz<10], kde=False)
plt.show()