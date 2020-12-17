# Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
	numero= random.randint(0,50)
	vetor.append(numero)


plt.boxplot(vetor)
plt.title("Grafico Boxplot")


plt.show()