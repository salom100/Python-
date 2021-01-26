import numpy as np 

m = np.array([10,15,25,5])

diff = np.diff(m)

print(diff)


#Calcule a diferença discreta da seguinte matriz duas vezes:
diff2 = np.diff(m, n=2)

print(diff2)