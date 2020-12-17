import random

#random.seed(1)

'''
	Ele gera numeros aleatorios ou entao escolhe um valor de uma determinada lista
	para numeros a função random.randint(inicio,fim)
	para objetos na lista random.choice(nomelista)
'''
numero = random.randint(0,10)
print(numero)

lista = [8,7,45]
escolha = random.choice(lista)
print(escolha)