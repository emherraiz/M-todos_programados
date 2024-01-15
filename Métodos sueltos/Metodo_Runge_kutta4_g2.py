import math
import os
import matplotlib.pyplot as plt
import numpy as np

# Ecuación de Bessel
def funcionBessel(x, u, v, n = 1):
    # Esta n no es absoluta, puede cambiar dependiendo de nuestro problema
    return v , - ((1/x)*v + (1 - (n**2 / x**2))*u)

# Ecuación de Legendre
def funcionLegendre(x, u, v, n = 0):
        # Esta n no es absoluta, puede cambiar dependiendo de nuestro problema
    n = 0
    return v, (2*x / (1-x**2)) * v - ((n*(n+1)) / (1-x**2)) * u

def Polinomio_chebyshev(x, u, v, n):
    return v, v * (x/(1-x**2)) - u * (n**2 / (1-x**2))

def plano_de_fases_2(x, u, v):
        return v, u - u**2

def Valor_inicial(n):
    suma = 0
    for m in range(math.floor(n/2)+1):
        suma += ((-1)**m) * (math.factorial(n - m - 1) / (math.factorial(m) * math.factorial(n - 2*m - 1))) * (-2)**(n-2*m-1)

    return n/2 * suma

def polinomio_jacobi(x, u, v, n = 1, alfa = 1.5, beta = 1):
    return v, - ((v*(beta - alfa - x*(2 + alfa + beta)) + u*(n*(n + alfa + beta + 1))) / (1 - x**2))


def nave_gia(x, u, v, a):
    return v, 





funcion = polinomio_jacobi

# Valores iniciales
xi = float(input('Introduce el valor inicial de x:\n> '))
xf = float(input('Introduce el valor final de nuestra región de x:\n> '))
# Número de pasos
n = int(input('Introduce el número de pasos:\n>'))

# Tamaño del paso
h = (xf - xi) / n

for n1 in [1, 2, 3, 4, 5]:
    beta = 1
    alfa = 1.5
    ui = -1**n1 * (math.factorial(n1 + beta) / (math.factorial(n1) * math.factorial(beta)))
    vi = ((-1)**n1 / 2) * (math.factorial(n1 + beta) / (math.factorial(n1 - 1) * math.factorial(beta))) * (1 + beta*(n + alfa))




    # Espacio donde trabajamos
    x = np.linspace(xi, xf, int(n+1))

    u = []
    u.append(ui)

    v = []
    v.append(vi)

    # Pesos
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6




    for i in range(n):
        k11, k12 = funcion(x[i], u[i], v[i], n1)
        k21, k22 = funcion(x[i] + h/2, u[i]+ h*k11/2, v[i]+ h*k12/2, n1)
        k31, k32 = funcion(x[i] + h/2, u[i]+ h*k21/2, v[i]+ h*k22/2, n1)
        k41, k42 = funcion(x[i] + h,  u[i]+ h*k31, v[i]+ h*k32, n1)
        u.append(u[i] + h*(a1*k11+a2*k21+a3*k31+a4*k41))
        v.append(v[i] + h*(a1*k12+a2*k22+a3*k32+a4*k42))


    print(v[-1])
    plt.plot(x, u)

plt.show()

