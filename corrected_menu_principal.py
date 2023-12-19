from EcuacionesPredefinidas import EcuacionesOrden1, EcuacionesOrden2
from Metodos_optimizados import MetodosEcuacionesOrden1, MetodosEcuacionesOrden2
import numpy as np
import matplotlib.pyplot as plt
import os
import math

def main():
    """
    Función principal que maneja el menú de usuario.
    """
    print('Bienvenido al solucionador de ecuaciones diferenciales.\nSelecciona el tipo de ecuación:')
    print('1 - Ecuación de grado 1\n2 - Ecuación de grado 2')
    opcion = int(input('>> '))

    if opcion == 1:
        manejar_primer_orden()
    elif opcion == 2:
        manejar_segundo_orden()
    else:
        print('Opción no válida. Por favor, elige 1 o 2.')

def manejar_primer_orden():
    """
    Función para manejar ecuaciones diferenciales de primer orden.
    """
    print('Selecciona la función a resolver:')
    # Las descripciones de las funciones se pueden mejorar para ser más descriptivas
    opciones_funcion = [
        "1 - y_prima = np.exp(x) / ((1 + np.exp(x))*y)",
        "2 - y_prima = (1 + 4*x*y) / (3*x**2)",
        "3 - y_prima = (2 - 3*x - y) / (x - 1)",
        "4 - y_prima = (x*y)/(x**2 + y**2)",
        "5 - y_prima = (x + y) / (x - y)"
    ]
    print('\n'.join(opciones_funcion))
    opcion_funcion = int(input('>> '))

    funciones = {
        1: EcuacionesOrden1.f_1,
        2: EcuacionesOrden1.f_2,
        3: EcuacionesOrden1.f_3,
        4: EcuacionesOrden1.f_4,
        5: EcuacionesOrden1.f_5
    }

    funcion = funciones.get(opcion_funcion)
    if not funcion:
        print('Función no válida.')
        return

    xi, xf, yi, n_pasos = solicitar_parametros_primer_orden()
    if n_pasos <= 0:
        print('El número de pasos debe ser un entero positivo.')
        return

    objeto = MetodosEcuacionesOrden1(xi, xf, yi, n_pasos, funcion)
    ejecutar_metodos_y_graficar(objeto, "Comparación de Métodos para Ecuaciones de Primer Orden")

def solicitar_parametros_primer_orden():
    """
    Solicita al usuario los parámetros para las ecuaciones de primer orden.
    """
    try:
        xi = float(input('Introduce el valor inicial de x:\n> '))
        xf = float(input('Introduce el valor final de x:\n> '))
        yi = float(input(f'Introduce el valor inicial de y({xi}):\n> '))
        n_pasos = int(input('Introduce el número de pasos:\n> '))
    except ValueError as e:
        print(f'Error: {e}')
        return None, None, None, None
    return xi, xf, yi, n_pasos

def manejar_segundo_orden():
    """
    Función para manejar ecuaciones diferenciales de segundo orden.
    """
    print('Selecciona la función a resolver:')
    opciones_funcion = [
        "1 - Función de Bessel",
        "2 - Función de Legendre",
        "3 - Polinomio de Chebyshev",
        "4 - Ecuaciones de Volterra",
        "5 - Plano de Fases 1",
        "6 - Plano de Fases 2",
        "7 - Polinomio de Jacobi",
        "8 - Control 2"
    ]
    print('\n'.join(opciones_funcion))
    opcion_funcion = int(input('>> '))

    funciones = {
        1: EcuacionesOrden2.funcion_bessel,
        2: EcuacionesOrden2.funcion_legendre,
        3: EcuacionesOrden2.polinomio_chebyshev,
        4: EcuacionesOrden2.ecuaciones_volterra,
        5: EcuacionesOrden2.plano_de_fases_1,
        6: EcuacionesOrden2.plano_de_fases_2,
        7: EcuacionesOrden2.polinomio_jacobi,
        8: EcuacionesOrden2.segundo_control
    }

    funcion = funciones.get(opcion_funcion)
    if not funcion:
        print('Función no válida.')
        return

    xi, xf, ui, vi, n_pasos = solicitar_parametros_segundo_orden(opcion_funcion)
    if n_pasos <= 0:
        print('El número de pasos debe ser un entero positivo.')
        return

    metodo = MetodosEcuacionesOrden2(xi, xf, ui, vi, n_pasos, funcion)

    print('Selecciona el método numérico:')
    opciones_metodos = [
        "1 - Método de Euler",
        "2 - Método de Runge Kutta orden 4",
    ]
    print('\n'.join(opciones_metodos))
    opcion_metodos = int(input('>> '))

    metodos = {
        1: metodo.EulerG2,
        2: metodo.RungeKutta4G2
    }

    metodo = metodos.get(opcion_metodos)
    x, u, v = metodo()

    graficar_segundo_orden(x, u, v)

def solicitar_parametros_segundo_orden(opcion_funcion):
    """
    Solicita al usuario los parámetros para las ecuaciones de segundo orden.
    """
    try:
        xi = float(input('Introduce el valor inicial de x:\n> '))
        xf = float(input('Introduce el valor final de x:\n> '))
        n_pasos = int(input('Introduce el número de pasos:\n> '))

        if opcion_funcion == 3:  # Polinomio de Chebyshev
            n = int(input('¿Cuál es el orden del polinomio?\n>> '))
            ui = (-1)**n
            vi = EcuacionesOrden2.valor_inicial(n)
        else:
            ui = float(input(f'Introduce el valor inicial de u({xi}):\n> '))
            vi = float(input(f'Introduce el valor inicial de v({xi}):\n> '))
    except ValueError as e:
        print(f'Error: {e}')
        return None, None, None, None, None
    return xi, xf, ui, vi, n_pasos

def ejecutar_metodos_y_graficar(objeto, titulo):
    """
    Ejecuta los métodos de un objeto de métodos y grafica los resultados.
    """
    metodos = [metodo for metodo in dir(objeto) if callable(getattr(objeto, metodo)) and not metodo.startswith("__")]

    plt.figure(figsize=(10, 6))

    for metodo in metodos:

        solucionador = getattr(objeto, metodo)
        print(solucionador)

    xi = objeto.xi
    xf = objeto.xf
    n = objeto.n
    h = objeto.h
    y_actual = objeto.yi

    x_valores = np.linspace(xi, xf, n+1)
    y_valores = []

    for x in x_valores[:-1]:
        y_valores.append(y_actual)
        y_actual += h * objeto.funcion(x, y_actual)
    y_valores.append(y_actual)  # Agregando el último valor de y
    print(metodo)
    # Ahora, 'x_valores' y 'y_valores' contienen los puntos calculados
    plt.plot(x_valores, y_valores, label=metodo)


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(titulo)
    plt.legend()
    plt.show()

def graficar_segundo_orden(x, u, v):
    """
    Grafica las soluciones de una ecuación diferencial de segundo orden.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, u, label='Solución u(x)')
    plt.plot(x, v, label='Solución v(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución Aproximada de la Ecuación Diferencial de 2do Orden')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
