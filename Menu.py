# Funciones predefinidas
from Ecuaciones_predefinidas import Ecuaciones_orden_1, Ecuaciones_orden_2

# Métodos
from Metodos import MetodosEcuacionesOrden1, MetodosEcuacionesOrden2

# Librerías que usamos
import numpy as np
import matplotlib.pyplot as plt
import os
import math

def main():
    print('1 - Ecuación de grado 1\n2 - Ecuación de grado 2')
    opcion = int(input('>> '))

    if opcion == 1:
        # Manejar ecuaciones de primer orden
        manejar_primer_orden()
    elif opcion == 2:
        # Manejar ecuaciones de segundo orden
        manejar_segundo_orden()
    else:
        print('Opción no válida. Por favor, elige 1 o 2.')

def manejar_primer_orden():
    print('Selecciona la función a resolver:')
    print('1 - y_prima = np.exp(x) / ((1 + np.exp(x))*y)')
    print('2 - y_prima = (1 + 4*x*y) / (3*x**2)')
    print('3 - y_prima = (2 - 3*x - y) / (x - 1)')
    print('4 - y_prima = (x*y)/(x**2 + y**2)')
    print('5 - y_prima = (x + y) / (x - y)')
    opcion_funcion = int(input('>> '))

    funciones = {
        1: Ecuaciones_orden_1.f_1,
        2: Ecuaciones_orden_1.f_2,
        3: Ecuaciones_orden_1.f_3,
        4: Ecuaciones_orden_1.f_4,
        5: Ecuaciones_orden_1.f_5
    }

    funcion = funciones.get(opcion_funcion)
    if not funcion:
        print('Función no válida.')
        return

    try:
        xi = float(input('Introduce el valor inicial de x:\n> '))
        xf = float(input('Introduce el valor final de x:\n> '))
        yi = float(input(f'Introduce el valor inicial de y({xi}):\n> '))
        n_pasos = int(input('Introduce el número de pasos:\n> '))

        if n_pasos <= 0:
            raise ValueError('El número de pasos debe ser un entero positivo.')

    except ValueError as e:
        print(f'Error: {e}')
        return

    objeto = MetodosEcuacionesOrden1(xi, xf, yi, n_pasos, funcion)

    metodos = [metodo for metodo in dir(objeto) if callable(getattr(objeto, metodo)) and not metodo.startswith("__")]

    plt.figure(figsize=(10, 6))

    for metodo in metodos:
        solucionador = getattr(objeto, metodo)
        x, y = solucionador()
        plt.plot(x, y, label=f'{metodo}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparación de Métodos para Ecuaciones de Primer Orden')
    plt.legend()
    plt.show()

def manejar_segundo_orden():
    print('Selecciona la función a resolver:')
    print('1 - Función de Bessel')
    print('2 - Función de Legendre')
    print('3 - Polinomio de Chebyshev')
    opcion_funcion = int(input('>> '))

    funciones = {
        1: Ecuaciones_orden_2.funcionBessel,
        2: Ecuaciones_orden_2.funcionLegendre,
        3: Ecuaciones_orden_2.Polinomio_chebyshev
    }

    funcion = funciones.get(opcion_funcion)
    if not funcion:
        print('Función no válida.')
        return

    try:
        xi = float(input('Introduce el valor inicial de x:\n> '))
        xf = float(input('Introduce el valor final de x:\n> '))
        n_pasos = int(input('Introduce el número de pasos:\n> '))

        if opcion_funcion == 3:
            n = int(input('¿Cuál es el orden del polinomio?\n>> '))
            ui = (-1)**n
            vi = Ecuaciones_orden_2.Valor_inicial(n)
        else:
            ui = float(input(f'Introduce el valor inicial de y({xi}):\n> '))
            vi = float(input(f'Introduce el valor inicial de y\'({xi}):\n> '))

        if n_pasos <= 0:
            raise ValueError('El número de pasos debe ser un entero positivo.')

    except ValueError as e:
        print(f'Error: {e}')
        return

    # Crear una instancia del método y ejecutar
    metodo = MetodosEcuacionesOrden2(xi, xf, ui, vi, n_pasos, funcion)
    x, u, v = metodo.RungeKutta4G2()  # Ejemplo usando Runge-Kutta de 4to orden

    # Visualizar los resultados
    plt.plot(x, u, label='Solución u(x)')
    plt.plot(x, v, label='Solución v(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución Aproximada de la Ecuación Diferencial de 2do Orden')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


