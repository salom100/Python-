import matplotlib.pyplot as plt

x=[1,3,5,7,9]
y=[2,3,7,1,0]

titulo = "Scatterplot: grafico de dispersão"
X="Eixo X"
Y="Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(X)
plt.ylabel(Y)

'''para fazer o grafico de pontos usamos o plt.scatter 
   x= a lista de colunas que ha 
   y= o valor que cada coluna tem
   label = a legenda com o nome para identificação
   color = a cor que cada ponto vai ter, esta pode ser definida com apenas a letra inicial da cor 
'''

'''
	Pesquise ma documentação oficial do matplot para poder ver que existem varias formas de estilo
	para que o grafico seja exibido 
	
	marker= define como cada ponto ira ser exibido (forma geometrica ou coisas do tipo)
	s= define o tamanho que cada ponto vai ter

	color= tem por padrao so necessitar da primeira letra (ver documentação das cores)
			Tambem se pode definir a cor atraves de "#990000 no padrao rgb sendo assim 2 casas sao pra R e G e B "

	linestyle= tem padroes de estilo de linha que sera exibido, ver na documentação

'''

plt.scatter(x,y,label="Meus pontos",color="r",marker=".")
plt.plot(x,y, color="k", linestyle=":")# estou utilizando ela para combar com o grafico de ponto ligando eles com linhas
plt.legend() # faz a legenda aparecer para poder exibir o Meus pontos
plt.show() # exibe tudo que foi estabelecido

''' plt.savefig salva o grafico que eu criei na mesma pasta do arquivo que executa
 eu passo como atributo o nome mais a extensao que pode ser png ou pdf ou entre outras, 
 sendo que quando vou salvar em formato de imagem a resolução pode nao sair tao boa, mas 
 eu posso configurar isso usando o dpi= numero de resolução

 sendo assim ficaria assim 
 plt.savefig("Figura1.png", dpi=300)

 o padrao geralmente é 300 mas pode ocorrer de alguma empresa requisitar uma maior resolução
''' 
plt.savefig("GraficoSalvo.pdf")


'''
	Exemplos da documentação 
	https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

	A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).



color:	cor (ver exemplos abaixo)

label:	rótulo

linestyle:	estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker:	marcador (ver exemplos abaixo)



CORES (color)
'b'	blue

'g'	green

'r'	red

'c'	cyan

'm'	magenta

'y'	yellow

'k'	black

'w'	white



Marcadores (marker)
'.'	point marker

','	pixel marker

'o'	circle marker

'v'	triangle_down marker

'^'	triangle_up marker

'<'	triangle_left marker

'>'	triangle_right marker

'1'	tri_down marker

'2'	tri_up marker

'3'	tri_left marker

'4'	tri_right marker

's'	square marker

'p'	pentagon marker

'*'	star marker

'h'	hexagon1 marker

'H'	hexagon2 marker

'+'	plus marker

'x'	x marker

'D'	diamond marker

'd'	thin_diamond marker

'|'	vline marker

'_'	hline marker





Tipos de linha (linestyle)
'-'	solid line style

'--'	dashed line style

'-.'	dash-dot line style

':'	dotted line style

'''