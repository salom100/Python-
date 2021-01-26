import numpy as np 

#seno
seno = np.sin(np.pi/2)
print(seno)

#SENO em Matrizes

matriz = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
senos = np.sin(matriz)
print("Senos")
print(senos)

#graus em radianos
m = np.array([90,180,270,360])

x= np.deg2rad(m)
print("Graus em radianos")
print(x)

#Radianos em graus
radianos = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
graus = np.rad2deg(radianos)
print("Radianos em graus")
print(graus)

#Encontrando angulos
print("\n Encontrando angulos")
arcoseno = np.arcsin(1.0)
print(arcoseno)

#angulos de cada valor da matriz
arr = np.array([1,-1,0.1])
senosArr = np.arcsin(arr)
print("\nAngulos de cada valor da matriz")
print(senosArr)

#Hipotecas
base = 3 #valores basicos
perp = 4 #valores perpendiculares

hipo = np.hypot(base,perp)
print("Hipotecas:",hipo)