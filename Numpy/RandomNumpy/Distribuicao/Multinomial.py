#DISTRIBUIÇÂO MULTINOMIAL
'''
    Generalização da distribuição binomial
    Descreve os resultados de cenarios multinomiais ex: tipo de sangue

    constituido por 3 parametros
    n= numero de resultados possiveis
    pvals= Lista de probabilidades de resultados
    size = a forma da matriz retornada
'''

from numpy import random

matriz= random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])

print(matriz)