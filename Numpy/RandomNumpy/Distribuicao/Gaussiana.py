from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb 


# random.normal() Possui 3 parametros
# size = matriz que queremos que retorne
# loc = media 
# scale = desvio padrao



matriz = random.normal(size=[2,3])

print(matriz)

#gerando uma distribuição normal aleatoria
M = random.normal(loc=1, scale=2, size=(2,3))
print("\n\nMatriz aleatoria gaussiana com media=1 desvioPadrao=2")
print(M)

#VISUALIZAÇÃO DA DISTRIBUIÇÃO NORMAL
sb.distplot(random.normal(size=1000, loc= 1, scale= 2), hist=False)

plt.show()
