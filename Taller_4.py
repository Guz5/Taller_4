

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generar datos para el tornado
theta = np.linspace(0, 10*np.pi, 1000)
z = np.linspace(-2, 2, 1000)
theta, z = np.meshgrid(theta, z)
x = z * np.sin(theta)
y = z * np.cos(theta)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el tornado
ax.plot_surface(x, y, z, cmap='coolwarm')

# Etiquetas de los ejes y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Tornado en 3D')

# Mostrar el gráfico
plt.show()

