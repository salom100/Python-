import matplotlib.pyplot as plt

x = [1,2,3,4,5] # quantidade de variaveis ou seja numeração das barras
y = [10,2,5,6,7] #tamanho das barras 

titulo = "Grafico de barras" #titulo do grafico
eixox= "Eixo X" # titulo do wixo x
eixoy= "Eixo Y" # titulo do eixo y

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.xlabel(eixoy)

plt.bar(x,y) # plt.bar que cria o grafico de barras
plt.show()