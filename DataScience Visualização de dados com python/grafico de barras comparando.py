import matplotlib.pyplot as plt # esse plt pode ser substituido, é so um apelido para nao ficar extenso demais 

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = "Grafico de barras 2"
x="Eixo X"
y="Eixo Y"

#titulos
plt.title(titulo)
plt.xlabel(x)
plt.xlabel(y)


'''Na hora que ele esta plotando os graficos para identificarmos o que representa cada um
	usamos o label = "titulo ou grupo"
	e depois plotamos ele usando o plt.legend()
'''
plt.bar(x1,y1, label ="Grupo 1")
plt.bar(x2,y2, label ="Grupo 2")
plt.legend()

plt.show()
