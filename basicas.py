# Importar la biblioteca 
import numpy as np

a =  np.array ([5,10,15,20,25])
print (a)

b = np.array ([3,4,7,9,56])
print (b)

c = a-b
print (c)

c = a + b
print (c)

c = a * b
print (c)

c = a**b  # Es el elevado
print (c)

c = np.sin (b)
print (c)

c = (b>6)
print (c)

c = a @ b  # Es el producto punto 
print (c)


c = a.min() # El valor mínimo
print(c)

c=a.mean()
print(c)

a = np.array([[-42,5,25,5,6],[5,8,52,7,1]])
print(a.min())


# Raíz
print (np.sqrt(a))  

# Exponencial
print (np.exp(a))

