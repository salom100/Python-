'''
Faça um programa que receba duas notas digitadas pelo usuário. 
Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
'''
nota1 = float(input("Digite a sua primeira nota"))
nota2 = float(input("Digite a sua segunda nota"))

media = (nota1+nota2)/2

if media >= 6:
	print("Voce foi aprovado com media igual a: ",media)
else :
	print("Voce foi reprovado, sua media é: ",media)