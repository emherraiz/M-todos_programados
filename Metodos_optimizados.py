import numpy as np

class MetodosEcuacionesOrden1:
    """
    Clase para resolver ecuaciones diferenciales de primer orden utilizando diferentes métodos numéricos.

    Atributos:
        xi (float): Valor inicial de x.
        xf (float): Valor final de x.
        yi (float): Valor inicial de y.
        n (int): Número de pasos.
        h (float): Tamaño del paso.
        funcion (callable): Función que define la ecuación diferencial.
    """

    def __init__(self, xi, xf, yi, n, funcion):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n debe ser un entero positivo")
        if xf <= xi:
            raise ValueError("xf debe ser mayor que xi")

        self.xi = xi
        self.xf = xf
        self.yi = yi
        self.n = n
        self.h = (xf - xi) / n
        self.funcion = funcion

    def Euler(self):
        # Sería lo mismo que el desarrollo de Taylor de primer orden
        x = np.linspace(self.xi, self.xf, self.n+1)
        y = [self.yi] + [0] * self.n
        for i in range(self.n):
            y[i + 1] = y[i] + self.h * self.funcion(x[i], y[i])
        return x, y

    def PredictorCorrector(self):
        x = np.linspace(self.xi, self.xf, self.n+1)
        y = [self.yi] + [0] * self.n
        for i in range(self.n):
            predictor = y[i] + self.h * self.funcion(x[i], y[i])
            y[i + 1] = y[i] + 0.5 * self.h * (self.funcion(x[i], y[i]) + self.funcion(x[i+1], predictor))
        return x, y

    def RungeKutta2(self):
        x = np.linspace(self.xi, self.xf, self.n+1)
        y = [self.yi] + [0] * self.n
        for i in range(self.n):
            k1 = self.funcion(x[i], y[i])
            k2 = self.funcion(x[i] + 0.5 * self.h, y[i] + 0.5 * self.h * k1)
            y[i + 1] = y[i] + self.h * k2
        return x, y

    def RungeKutta4(self):
        x = np.linspace(self.xi, self.xf, self.n+1)
        y = [self.yi] + [0] * self.n
        for i in range(self.n):
            k1 = self.funcion(x[i], y[i])
            k2 = self.funcion(x[i] + 0.5 * self.h, y[i] + 0.5 * self.h * k1)
            k3 = self.funcion(x[i] + 0.5 * self.h, y[i] + 0.5 * self.h * k2)
            k4 = self.funcion(x[i] + self.h, y[i] + self.h * k3)
            y[i + 1] = y[i] + (self.h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return x, y

class MetodosEcuacionesOrden2:
    """
    Clase para resolver ecuaciones diferenciales de segundo orden utilizando diferentes métodos numéricos.

    Atributos:
        xi (float): Valor inicial de x.
        xf (float): Valor final de x.
        ui (float): Valor inicial de u.
        vi (float): Valor inicial de v.
        n (int): Número de pasos.
        h (float): Tamaño del paso.
        funcion (callable): Función que define la ecuación diferencial.
    """
    def __init__(self, xi, xf, ui, vi, n, funcion):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n debe ser un entero positivo")
        if xf <= xi:
            raise ValueError("xf debe ser mayor que xi")
        self.xi = xi
        self.xf = xf
        self.ui = ui
        self.vi = vi
        self.n = n
        self.h = (xf - xi) / n
        self.funcion = funcion

    def EulerG2(self):
        x = np.linspace(self.xi, self.xf, self.n+1)
        u = [self.ui] + [0] * self.n
        v = [self.vi] + [0] * self.n
        for i in range(self.n):
            u[i + 1] = u[i] + self.h * v[i]
            v[i + 1] = v[i] + self.h * self.funcion(x[i], u[i], v[i])
        return x, u, v

    def RungeKutta4G2(self):
        x = np.linspace(self.xi, self.xf, self.n+1)
        u = [self.ui] + [0] * self.n
        v = [self.vi] + [0] * self.n
        for i in range(self.n):
            k11, k12 = self.funcion(x[i], u[i], v[i])
            k21, k22 = self.funcion(x[i] + 0.5 * self.h, u[i] + 0.5 * self.h * k11, v[i] + 0.5 * self.h * k12)
            k31, k32 = self.funcion(x[i] + 0.5 * self.h, u[i] + 0.5 * self.h * k21, v[i] + 0.5 * self.h * k22)
            k41, k42 = self.funcion(x[i] + self.h, u[i] + self.h * k31, v[i] + self.h * k32)
            u[i + 1] = u[i] + (self.h / 6) * (k11 + 2 * k21 + 2 * k31 + k41)
            v[i + 1] = v[i] + (self.h / 6) * (k12 + 2 * k22 + 2 * k32 + k42)
        return x, u, v
