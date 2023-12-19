# Método de Euler.

import numpy as np
import matplotlib.pyplot as plt

# Nuestra y'
def f_1(x, y):
    return np.exp(x) / ((1 + np.exp(x))*y)

def f_2(x, y):
    return (1 + 4*x*y) / (3*x**2)

def f_3(x, y):
    return (2 - 3*x - y) / (x - 1)

def f_4(x, y):
    return (x*y)/(x**2 + y**2)

def f_5(x, y):
    return (x + y) / (x - y)


funcion = f_5

# Definimos la región en la que trabajamos
xi = float(input('Introduce el valor inicial de x:\n> '))
xf = float(input('Introduce el valor final de nuestra región de x:\n> '))
yi = float(input(f'Introduce el valor en y({xi}):\n > '))


# Número de pasos
n = int(input('Introduce el número de pasos:\n> '))

# Tamaño del paso
h = (xf - xi) / n

# Espacio donde trabajamos
x = np.linspace(xi, xf, int(n+1))

# Solución numérica
y = []
y.append(yi)

for i in range(n):
    y.append(y[i] + h*funcion(x[i], y[i]))

# Observamos el resultado de nuestra última iteración
print(y[-1])

plt.plot(x, y, 'r')
plt.show()






