#visualização de dados em python

import matplotlib.pyplot as plt

x = [1,2,5]
y = [2,3,7]

#titulo
plt.title("Titulo de Grafico no python")

#Eixos
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.plot(x,y) # plt.plot que cria o grafico de linhas

plt.show()