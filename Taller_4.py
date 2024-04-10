#Importar la biblioteca
import numpy as np

#un metodo de crear arreglos ndarray es usando una lista normalita

miLista = [3,5,7,9]

miArreglo = np.array(miLista)

#Dimensiones eje
print ("Dimensiones:", miArreglo.ndim)

#Dimensiones eje y longitud
print ("Eje y Longitud:", miArreglo.shape)

#Elementos
print ("Elementos:", miArreglo.size)

#Tipos de elementos
print ("Tipos de elementos:", miArreglo.dtype)



miArreglo2 = np.array([3,5,8,14])

print (miArreglo2.dtype)



#Crear arreglos de dos dimensiones a partir de listas

miLista3 = [(5,8,7,62), (3,2,5,1)]

miArreglo3 = np.array(miLista3)
print (miArreglo3)
print (miArreglo3.ndim)
print (miArreglo3.shape)
print (miArreglo3.size)

