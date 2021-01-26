import numpy as np


print("Resultados hiperbolicos")

hiperbolica1= np.sinh(np.pi/2)
print("np.sinh():",hiperbolica1)

matriz = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
hiperbolica2= np.cosh(matriz)
print("np.cosh()",hiperbolica2)

#Encontrando angulos a partir de valores hiperbolicos
hiperbolica3 = np.arcsinh(1.0)
print("np.arcsinh():",hiperbolica3)

#encontrando angulos em matriz com valores hiperbolicos
matriz2 = np.array([0.1, 0.2, 0.5])
hiperbolica4 = np.arctanh(matriz2)
print("np.arctanh():",hiperbolica4)
