
#Q= (q0,q1,q2,q3) -> estados
#E= (abbaabb)-> entrada finita
#R= (a,b,x)->alfabeto
#Q0= (q0)-> estado inicial
#x=(x)->simbolo do vazio
#F= (q3)->estado final

#Dicionario dinamico
#d[""+chave] = valor
#Onde "d" é o dicionário, "chave" é a chave do elemento ("primeiro", "segundo" e "terceiro") e "valor" é o valor do elemento ("janeiro", "fevereiro" e "março").
#print(c1.__dict__) printar os dados do do objeto em formato de dicionario

import os

Pontos = []
while 1<2:
	os.system("cls")
	print("Bem vindo a maquina de turing")
	opcao = int(input("1) Criar uma maquina de turing \n2) Executar a maquina de turing \n3)Sair do programa"))
	if opcao == 1: #CRIANDO MAQUINA DE TURING
		Estados={}
		print("Criando maquina de turing")
		Nestados=int(input("Quantos estados devera haver ?"))
		i=0
		for i in range(i,Nestados,1):
			os.system("cls")
			lista=[]
			Nome= input("Digite o nome Ex: q1,q2,q3,q4\n")
			Pontos.append(Nome)
			I= int(input("É um estado inicial ? 1)sim 2)nao"))
			if I == 1:
				lista.append("Inicial")
			v = int(input("possui simbolo do vazio  no estado? (1)sim (2)nao"))
			if v == 1:
				lista.append(input("Qual é o simbolo do vazio ?"))
				lista.append(input("Digite o estado que o vazio ira levar ex: q1,q2,q3"))
			letras= int(input("Quantas letras havera ?"))
			j=0
			for j in range(j,letras,1):
				lista.append(input("Digite a letra"))
				lista.append(input("Digite o estado que a letra vai levar ex: q1,q2,q3"))
			F= int(input("É um estado final ? 1)sim 2)nao"))
			if F == 1:
				lista.append("Final")

			Estados[""+Nome]=lista

		print("Estados Criados")
		print(Estados)

		

		
		seila=input("Digite qualquer tecla para continuar")

	elif opcao == 2: # EXECUTANDO MAQUINA DE TURING
		i=0
		print("Executando maquina de turing")
		entrada = []
		palavra = input("Digite a palavra que ira ser processada")
		for i in range(i,len(palavra)):
			entrada.append(palavra[i])

		j=0
		for j in range(j,len(entrada)):
			letra = entrada[j]
			os.system("cls")
			
			if j == 0:	
				k=0
				for k in range(k,len(Pontos)):
					ini= Estados[""+Pontos[k]].count("Inicial")
					if ini == 1:
						Busca= Pontos[k]
			print(letra+"--> leitura da fita na posição atual")
			print(Busca+" -->Estado Inicial ou acessado no momento")
			valida = Estados[""+Busca].count(letra)
			
			if valida >=1 :
				pos = Estados[""+Busca].index(letra)
				print(pos)
				Busca= Estados[""+Busca][pos+1]
				print(Busca +" --> O proximo estado a ser buscado")
				seila=input("proximo passo-->")
			else:
				seila=input("A maquina de Turing nao aceita a palavra")
				break

		letra="X"
		valida = Estados[""+Busca].count(letra)
		if valida >=1 :
			pos = Estados[""+Busca].index(letra)
			print(pos)
			Busca= Estados[""+Busca][pos+1]
			print(Busca +" --> O proximo estado a ser buscado")
			seila=input("proximo passo-->")
			final = Estados[""+Busca].count("Final")
			if final >= 1:
				seila= input("A palavra foi aceita com sucesso na maquina de Turing\nAperte qualquer tecla para voltar ao menu")
			else:
				seila= input("A maquina de Turing nao aceitou a palavra")	
		else:
			final = Estados[""+Busca].count("Final")
			if final >= 1:
				input("A palavra foi aceita com sucesso na maquina de Turing\nAperte qualquer tecla para voltar ao menu")
			else:
				seila= input("A palavra nao foi aceita na maquina de turing")



		seila=input("Digite qualquer tecla para continuar")

	elif opcao ==3:
		seila=input("Finalizando a maquina de Turing, aperte qualquer tecla para sair")
		break;
	else:
		seila=input("Opção selecionada nao é valida, aperte qualquer tecla para voltar ao menu")