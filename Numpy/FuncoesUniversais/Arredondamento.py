#Arredondamento
'''
    5 formas de arrendondar
    truncamento
    consertar
    arredondamento
    chão
    teto
'''

#TRUNCAMENTO
import numpy as np

trunc =np.trunc([-3.1504,3.7522])
print("Truncamento(trunc):",trunc)

fix= np.fix([-3.1425,3.7895])
print("Truncamento(fix):",fix)

#ARREDONDAMENTO
around = np.around([3.1555,2])
print("Arredondamento(around):",around)

#CHAO
chao = np.floor([-3.1555,3.6667])
print("Chao(floor):",chao)

#TETO
teto = np.ceil([-3.1554,3.756])
print("Teto(ceil):",teto)