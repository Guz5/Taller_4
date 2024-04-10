#Importar la biblioteca
import numpy as np

#Crear arreglos de dos dimensiones a partir de listas


miLista = [(5,8,7,62), (3,2,5,1)]

miArreglo = np.array(miLista)
print (miArreglo)
print (miArreglo.ndim)
print (miArreglo.shape)
print (miArreglo.size)