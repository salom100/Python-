'''Escreva um programa que resolva uma equação de segundo grau.   '''

# a2 + bx +c
# (-b +- sqrt(b2-4ac))/

from math import sqrt

a= int(input("digite o valor de a:"))
b= int(input("digite o valor de b:"))
c= int(input("digite o valor de c:"))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b +raiz_delta)/(2*a)
x2 = (-b -raiz_delta)/(2*a)

print("x1 = %f"%x1)
print("x2 = %f"%x2)
