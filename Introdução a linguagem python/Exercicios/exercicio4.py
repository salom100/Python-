'''Escreva um programa que ordene uma lista numérica com três elementos.   '''
'''
lista = [5,7,1]

lista.sort()
print(lista)

'''
itens = int(input("quantos numeros quer na sua lista ?: "))
i=0

lista= []

while i < itens:
	numero=int(input("Digite o numero "))
	lista.append(numero)
	i+=1
'''pode ser feito apenas usando a função ja pre estabelecida
lista.sort()
print(lista)
'''
for i in range(len(lista)):
	menor =i
	for j in range(i+1, len(lista)):
		if lista[j] < lista[menor]:
			menor =j

	if lista[i] != lista[menor]:
		aux=lista[i]
		lista[i]=lista[menor]
		lista[menor]=aux

print (lista)