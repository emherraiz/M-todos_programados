import matplotlib.pyplot as plt
import numpy as np

def funcion(x, y):
    n = 0
    return (x+y) / (x-y)



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

# Pesos
a1 = 1/6
a2 = 1/3
a3 = 1/3
a4 = 1/6


for i in range(n):
    k1 = funcion(x[i], y[i])
    k2 = funcion(x[i] + h/2, y[i]+ h*k1/2)
    k3 = funcion(x[i] + h/2, y[i]+ h*k2/2)
    k4 = funcion(x[i] + h, y[i]+ h*k3)
    y.append(y[i] + h*(a1*k1+a2*k2+a3*k3+a4*k4))


# Observamos el resultado de nuestra última iteración
print(y[-1])

plt.plot(x, y, 'r')
plt.show()
