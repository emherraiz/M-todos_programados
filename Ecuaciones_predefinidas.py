import numpy as np


class Ecuaciones_orden_1():
    '''Ecuaciones de primer orden'''
    @staticmethod
    def f_1(x, y):
        return np.exp(x) / ((1 + np.exp(x))*y)

    # El ejemplo 2 lo podemos usar en taylor orden 2 puesto que ya tenemos sus derivadas parciales
    @staticmethod
    def f_2(x, y):
        return (1 + 4*x*y) / (3*x**2)

    # Derivada parcial en x
    @staticmethod
    def f_dx(x, y):
        return (4*y)/(3*x**2) - (8*x*y)/(3*x**3)

    # Derivada parcial en y
    @staticmethod
    def f_dy(x, y):
        return (4*x)/(3*x**2)

    @staticmethod
    def f_3(x, y):
        return (2 - 3*x - y) / (x - 1)

    @staticmethod
    def f_4(x, y):
        return (x*y)/(x**2 + y**2)

    @staticmethod
    def f_5(x, y):
        return (x + y) / (x - y)



class Ecuaciones_orden_2():
    '''Ecuaciones de 2do orden'''

    @staticmethod
    def funcionBessel(x, u, v, n = 1):
        # Esta n no es absoluta, puede cambiar dependiendo de nuestro problema
        return v , - ((1/x)*v + (1 - (n**2 / x**2))*u)

    # Ecuación de Legendre
    @staticmethod
    def funcionLegendre(x, u, v, n = 0):
            # Esta n no es absoluta, puede cambiar dependiendo de nuestro problema
        return v, (2*x / (1-x**2)) * v - ((n*(n+1)) / (1-x**2)) * u

    @staticmethod
    def Polinomio_chebyshev(x, u, v, n):
        return v, v * (x/(1-x**2)) - u * (n**2 / (1-x**2))

    @staticmethod
    def Valor_inicial(n):
        suma = 0
        for m in range(math.floor(n/2)+1):
            suma += ((-1)**m) * (math.factorial(n - m - 1) / (math.factorial(m) * math.factorial(n - 2*m - 1))) * (-2)**(n-2*m-1)

        return n/2 * suma
