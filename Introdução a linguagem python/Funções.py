'''
	Nota importante ao se utilizar funções, elas sempre devem estar no topo da pagina pois se colocadas no final a leitura do programa
	pode ser feita de forma erronea, nao reconhecendo que existe a função naquela hora que executa o codigo 	
'''
def soma(x,y):
	return x+y

def multiplicação(x,y):
	return x*y
s = soma(2,4)
m = multiplicação(4,4)
print("Chamada da função soma = ",s)
print("Chamada da função multiplicação = ",m)
print("Chamando a função soma com os resultados anteriores =",soma(s,m))