lista1 = ["maça","melao","social"]
lista2 = [1,2,3,4,5]
lista3 = ["abacaxi", 2, 9.89, True]

lista1.append("limao")

tamanho = len(lista1)

print(tamanho)
print(lista1)

if 3 in lista2:
	print("3 esta na lista")

del lista1[2:]
print(lista1)

del lista1[:]

# CRIANDO UMA LISTA 
lista4 =[]
lista4.append("Melao")
lista4.append("Boeing")
print(lista4)

# ORDENANDO LISTAS com SORT

lista = [123,5,4,5,87,145,15,541]
lista.sort() # ele ordena de forma crecente
print(lista)

lista.sort(reverse=True) # faz o reverso ele ordena de modo decrescente
print(lista)

lista.reverse()#ele inverte a lista
print(lista)

print("ORDENANDO LISTA DE PALAVRAS")
# Tambem é possivel usar o sort para listas com palavras
lista5 = ["feijao","macarrao","arroz","batata"]
lista5.sort()
print(lista5)