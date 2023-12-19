# Metodo de Euler Grado 2
import math
import matplotlib.pyplot as plt
import numpy as np

def funcion(x, u, v):
    n = .1
    return - ((1/x)*v + (1 - (n**2 / x**2))*u)



# Valores iniciales
xi = float(input('Introduce el valor inicial de x:\n> '))
xf = float(input('Introduce el valor final de nuestra región de x:\n> '))
ui = float(input(f'Introduce el valor en y({xi}):\n > '))
vi = float(input(f'Introduce el valor en y_prima({xi}):\n > '))


# Número de pasos
n = int(input('Introduce el número de pasos:\n>'))

# Tamaño del paso
h = (xf - xi) / n

# Espacio donde trabajamos
x = np.linspace(xi, xf, int(n+1))

# y
u = []
u.append(ui)

# y'
v = []
v.append(vi)


for i in range(n):
    u.append(u[i] + h*v[i])
    v.append(v[i] + h*funcion(x[i], u[i], v[i]))

print(v[-1])
plt.plot(x, u, 'r')
plt.show()

