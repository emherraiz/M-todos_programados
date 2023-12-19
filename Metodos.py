import numpy as np
# Métodos para ecuaciones de orden 1
class MetodosEcuacionesOrden1():
    def __init__(self, xi, xf, yi, n, funcion):
        self.xi = xi
        self.xf = xf
        self.yi = yi
        self.n = n
        self.h = (self.xf - self.xi) / self.n
        self.funcion = funcion


    def Euler(self):
        # Tamaño del paso

        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        # Solución numérica
        y = []
        y.append(self.yi)

        for i in range(self.n):
            y.append(y[i] + self.h*self.funcion(x[i], y[i]))

        return x, y

    def PredictorCorrector(self):
        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        y = []
        y.append(self.yi)

        z = []
        z.append(self.yi)

        for i in range(self.n):
            z.append(y[i] + self.h*self.funcion(x[i], y[i]))
            y.append(y[i] + (self.h/2) * (self.funcion(x[i], y[i]) + self.funcion(x[i+1], z[i+1])))

        return x, y

    '''
    def Taylor_orden_2(self, f_dx, f_dy):
        # Espacio donde trabajamos
        x = []
        x.append(self.xi)

        # Solución numérica
        y = []
        y.append(self.yi)

        for i in range(self.n+1):
            f_der_2 = f_dx(x[i], y[i]) + f_dy(x[i], y[i]) * self.funcion(x[i], y[i])
            y.append(y[i] + self.h*self.funcion(x[i], y[i]) + (self.h**2 /2) * f_der_2)
            x.append(x[i] + self.h)

        return x, y
    '''

    def RungeKutta2(self):
        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        # Solución numérica
        y = []
        y.append(self.yi)

        for i in range(self.n):
            k1 = self.funcion(x[i], y[i])
            k2 = self.funcion(x[i] + self.h/2, y[i]+ self.h*k1/2)
            y.append(y[i] + self.h*k2)

        return x, y

    def RungeKutta4(self):
        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        # Solución numérica
        y = []
        y.append(self.yi)

        # Pesos
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6


        for i in range(self.n):
            k1 = self.funcion(x[i], y[i])
            k2 = self.funcion(x[i] + self.h/2, y[i]+ self.h*k1/2)
            k3 = self.funcion(x[i] + self.h/2, y[i]+ self.h*k2/2)
            k4 = self.funcion(x[i] + self.h, y[i]+ self.h*k3)
            y.append(y[i] + self.h*(a1*k1+a2*k2+a3*k3+a4*k4))

        return x, y


class MetodosEcuacionesOrden2():

    def __init__(self, xi, xf, ui, vi, n, funcion):
        self.xi = xi
        self.xf = xf
        self.ui = ui
        self.vi = vi
        self.n = n
        self.h = (self.xf - self.xi) / self.n
        self.funcion = funcion


    # Métodos para ecuaciones de orden 2
    def EulerG2(self):
        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        # y
        u = []
        u.append(self.ui)

        # y'
        v = []
        v.append(self.vi)


        for i in range(self.n):
            u.append(u[i] + self.h*v[i])
            v.append(v[i] + self.h*self.funcion(x[i], u[i], v[i]))

        return x, u, v


    def RungeKutta4G2(self):
        # Espacio donde trabajamos
        x = np.linspace(self.xi, self.xf, int(self.n+1))

        # y
        u = []
        u.append(self.ui)

        # y'
        v = []
        v.append(self.vi)

        # Pesos
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6


        for i in range(self.n):
            k11, k12 = self.funcion(x[i], u[i], v[i])
            k21, k22 = self.funcion(x[i] + self.h/2, u[i]+ self.h*k11/2, v[i]+ self.h*k12/2)
            k31, k32 = self.funcion(x[i] + self.h/2, u[i]+ self.h*k21/2, v[i]+ self.h*k22/2)
            k41, k42 = self.funcion(x[i] + self.h,  u[i]+ self.h*k31, v[i]+ self.h*k32)
            u.append(u[i] + self.h*(a1*k11+a2*k21+a3*k31+a4*k41))
            v.append(v[i] + self.h*(a1*k12+a2*k22+a3*k32+a4*k42))

        return x, u, v
