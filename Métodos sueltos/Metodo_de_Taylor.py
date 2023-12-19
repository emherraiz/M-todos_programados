# Metodo de Taylor solo orden 2
# Nota: En orden 1 es el método de Euler
import numpy as np
import matplotlib.pyplot as plt

# Primera derivada
def funcion(x, y):
    return (1 + 4*x*y)/(3*x**2)

# Derivada parcial en x
def f_dx(x, y):
    return (4*y)/(3*x**2) - (8*x*y)/(3*x**3)

# Derivada parcial en y
def f_dy(x, y):
    return (4*x)/(3*x**2)

# Definimos la región en la que trabajamos
xi = float(input('Introduce el valor inicial de x:\n> '))
xf = float(input('Introduce el valor final de nuestra región de x:\n> '))
yi = float(input(f'Introduce el valor en y({xi}):\n > '))


# Número de pasos
n = int(input('Introduce el número de pasos:\n> '))


# Tamaño del paso
h = (xf - xi) / n

# Espacio donde trabajamos
x = []
x.append(xi)

# Solución numérica
y = []
y.append(yi)

for i in range(n+1):
    f_der_2 = f_dx(x[i], y[i]) + f_dy(x[i], y[i]) * funcion(x[i], y[i])
    y.append(y[i] + h*funcion(x[i], y[i]) + (h**2 /2) * f_der_2)
    x.append(x[i] + h)

# Representar la solución numérica
plt.plot(x, y, label='Solución numérica')
plt.show()
