x=1
print("Laço de repetição do tipo While de 1 ate 10")
while x<10:
	print(x)
	x+=1

'''Listas sao variaveis aonde eu posso colocar mais de uma valor dentro delas'''
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [1,"hello","arara",0.98]

print("\nLaço de repetição FOR para a lista 1\n")
for i in lista1:
	print(i)
print("\nLaço de repetição FOR para a lista 1\n")
for i in lista2:
	print(i)
print("\nLaço de repetição FOR para a lista 1\n")
for i in lista3:
	print(i)


'''O comando Range é usado ou funciona como uma lista que é criada entre os intervalos que eu desejo
	Sendo assim a sintaxe fica:
	Range(Inicio,Fim,Intervalo_de_saltos)

	O intervalo de saltos é opcional 
'''

print("\nComando FOR usado junto ao comando RANGE\n")
for i in range(10,20,2):
	print(i)