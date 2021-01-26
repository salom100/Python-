import numpy as np

matriz = np.array([40,41,42,43])

x= [True,False,True,False]

# ele pega somente o valores correspondentes a True 
NovaMatriz= matriz[x]

print(NovaMatriz)

#CRIAÇÃO DE MATRIZ DE FILTRO
Filtro = []
FiltroPar = []

for i in matriz:
    if i >41:
        Filtro.append(True)
    else :
        Filtro.append(False)
    
    if i%2 == 0:
        FiltroPar.append(True)
    else:
        FiltroPar.append(False)

''' Descomente para ver o que acima faz
MatrizFiltrada = matriz[Filtro]
print("Filtro: ",Filtro)
print("Matriz Filtrada: ",MatrizFiltrada)

MatrizFiltradaPar = matriz[FiltroPar]
print("Filtro Par: ",FiltroPar)
print("Matriz Filtrada",MatrizFiltradaPar)
'''

# Criando filtro direto do array
fil = matriz>41

Mfil = matriz[fil]

print(fil)
print(Mfil)

Matriz2= np.array([1,2,3,4,5,6,7])
FiltroPar2 = Matriz2%2 == 0 

Mfil2 = Matriz2[FiltroPar2]

print(FiltroPar2)
print(Mfil2)