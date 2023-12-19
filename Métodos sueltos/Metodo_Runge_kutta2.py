import matplotlib.pyplot as plt
import numpy as np

def funcion(x, y):
    return np.exp(x) / ((1 + np.exp(x))*y)



# Valores iniciales
xi = float(input('Introduce el valor inicial de x:\n> '))
xf = float(input('Introduce el valor final de nuestra región de x:\n> '))
yi = float(input(f'Introduce el valor en y({xi}):\n > '))

# Número de pasos
n = int(input('Introduce el número de pasos:\n>'))

# Tamaño del paso
h = (xf - xi) / n

# Espacio donde trabajamos
x = np.linspace(xi, xf, int(n+1))

y = []
y.append(yi)

for i in range(n):
    k1 = funcion(x[i], y[i])
    k2 = funcion(x[i] + h/2, y[i]+ h*k1/2)
    y.append(y[i] + h*k2)
# Observamos el resultado de nuestra última iteración
print(y[-1])

plt.plot(x, y, 'r')
plt.show()
