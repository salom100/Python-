'''Escreva um programa que receba dois números e um sinal,
 e faça a operação matemática definida pelo sinal.   '''

while 1 :
	print("1) Realizar um calculo")
	print("2) Sair")
	opcao= int(input("opcao: "))
	if opcao == 1:
		print("Calculo matematico")
		n1= int(input("Digite o primeiro numero: "))
		n2= int(input("Digite o segundo numero: "))
		opera = input("Digite a operação(+,/,-,*):  ")

		if opera == "+":
			soma=n1+n2
			print("Operação soma foi escolhida, resultado é: ",soma)
		elif opera == "-":
			subtrai= n1-n2
			print("Operação subtração foi escolhida, resultado é: ",subtrai)
		elif opera == "*":
			multi=n1*n2
			print("multiplicação foi a operação, resultado é: ",multi)
		elif opera == "/":
			divi = n1/n2
			print("divisão foi a operação escolhida, resultado é: ",divi)
		else:
			print("Nenhuma operação conhecida para prosseguir calculo")

	elif opcao ==2:
		print("Finalizando programa")
		break
	else :
		print("Nenhuma das opções foi escolhida")