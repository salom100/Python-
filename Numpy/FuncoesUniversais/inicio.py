import numpy as np

x= [1,2,3,4]
y= [4,5,6,7]
z=[]

#SEM USAR UFUNCS
for i,j in zip(x,y):
    z.append(i+j)

print(z)

#USANDO UFUNCS
 

a= [1,2,3,4]
b= [4,5,6,7]
c= np.add(a,b)

print(c)