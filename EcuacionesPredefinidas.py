import numpy as np

class EcuacionesOrden1:
    """
    Clase que contiene ecuaciones diferenciales de primer orden.
    """

    @staticmethod
    def f_1(x, y):
        """Ecuación diferencial con función exponencial."""
        return np.exp(x) / ((1 + np.exp(x)) * y)

    @staticmethod
    def f_2(x, y):
        """Ecuación diferencial, útil para el método de Taylor de orden 2."""
        return (1 + 4 * x * y) / (3 * x**2)

    @staticmethod
    def f_dx(x, y):
        """Derivada parcial en x de f_2."""
        return (4 * y) / (3 * x**2) - (8 * x * y) / (3 * x**3)

    @staticmethod
    def f_dy(x, y):
        """Derivada parcial en y de f_2."""
        return 4 / (3 * x)

    @staticmethod
    def f_3(x, y):
        """Otra ecuación diferencial de primer orden."""
        return (2 - 3 * x - y) / (x - 1)

    @staticmethod
    def f_4(x, y):
        """Ecuación diferencial con términos cuadráticos."""
        return (x * y) / (x**2 + y**2)

    @staticmethod
    def f_5(x, y):
        """Ecuación diferencial con términos lineales."""
        return (x + y) / (x - y)


class EcuacionesOrden2:
    """
    Clase que contiene ecuaciones diferenciales de segundo orden.
    """

    @staticmethod
    def funcion_bessel(x, u, v, n=0):
        """Ecuación de Bessel para un valor dado de n."""
        return v, -((1 / x) * v + (1 - (n**2 / x**2)) * u)

    @staticmethod
    def funcion_legendre(x, u, v, n=0):
        """Ecuación de Legendre para un valor dado de n."""
        return v, (2 * x / (1 - x**2)) * v - ((n * (n + 1)) / (1 - x**2)) * u

    @staticmethod
    def polinomio_chebyshev(x, u, v, n):
        """Polinomio de Chebyshev para un valor dado de n."""
        return v, v * (x / (1 - x**2)) - u * (n**2 / (1 - x**2))

    @staticmethod
    def valor_inicial(n):
        """Calcula el valor inicial para un polinomio de Chebyshev."""
        suma = 0
        for m in range(np.floor(n / 2).astype(int) + 1):
            suma += ((-1)**m) * (np.math.factorial(n - m - 1) / (np.math.factorial(m) * np.math.factorial(n - 2 * m - 1))) * (-2)**(n - 2 * m - 1)

        return n / 2 * suma

    def ecuaciones_volterra(x, u, v, p = 3, q = 1, r = 2, s = 1):
        return p * u - q * u * v, -r * v + s * u * v

    def plano_de_fases_1(x, u, v):
        return -v + u * (1 - u**2 - v**2), u + v * (1 - u**2 * v**2)

    def plano_de_fases_2(x, u, v):
        return v, u - u**2

    def polinomio_jacobi(x, u, v, n = 1, alfa = 1.5, beta = 1):
        return v, - ((v*(-beta - alfa - x*(2 + alfa + beta)) - u*(n*(n + alfa + beta + 1))) / (1 - x**2))

    def segundo_control(x, u, v):
        return -4*v - 4*u + (np.exp(-2*x)) / (1 - x**2)
