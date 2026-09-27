import numpy as np

def f(x):
    """
    Función a integrar

    Args:
        x (float): punto a evaluar

    Returns:
        float, valor calculado

    Ejemplos:
        x = 1: 0.09070257317431829
        x = 2: 67.0272099812317
        x = 3: 731.5147394837903
        x = 4: 4080.170268054026
        x = 5: 15638.600527772234

    """
    return x**6 - (x**2) * np.sin(2 * x)
print(f"{"-" * 50}")
print(f"Función evaluada en distintos puntos a manera de prueba.")
print(f"Prueba: x = 1: {f(1)}. x = 2: {f(2)}. x = 3: {f(3)}. x = 4: {f(4)}. x = 5: {f(5)}.")

def gaussxw(N):
    """
    Devuelve los puntos según las raíces del polinomio de Legendre

    Args:
        N (int): número de puntos
    
    Returns:
        tupla: x, w, donde x son los puntos, y w los pesos

    Ejemplo:
        x, w = gaussxw(2)
        x = [-0.57735027  0.57735027], w = [1. 1.]
        len(x) -> 2, len(w) -> 2
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w
print(f"{"-" * 50}")
print(f"x y w originales.")
x, w = gaussxw(2)
print(f"x = {x}, w = {w}")

def gaussxwab(a, b, x, w):
    """
    Evalúa los puntos y pesos en el intervalo dado 

    Args:
        a (float): límite inferior de la integral
        b (float): límite superior de la integral
        x (array): puntuos a evaluar del intervalo
        w (array): pesos a evaluar del intervalo

    Returns:
        tupla: puntos y pesos en formato a, b

    Ejemplo:
        x, w = gaussxw(2)
        x_2, w_2 = gaussxwab(1.0, 3.0, x, w)
        x = [3.42264973 4.57735027], w = [1. 1.]
        len(x_2) -> 2, len(w_2) -> 2
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
print(f"{"-" * 50}")
print(f"Ajuste de x y w.")
x_2, w_2 = gaussxwab(1.0, 3.0, x, w)
print(f"x = {x_2}, w = {w_2}")
def integrarGaussiana(f, a, b, N):
    """
    Calcula la integral de una función mediante el método de cuadratura gaussiana

    Args:
        f (función): función a integrar
        a (float): límite inferior
        b (float): límite superior
        N (int): numero de puntos de gauss
    
    Returns:
        float: valor de la integral

    Ejemplo:
        for i in range(10):
            resultado = intergrarGaussiana(f, 1 , 3, i + 1)
            print(f"Para N= {i + 1} en resultado es: {resultado}")

        Para N= 1 en resultado es: 134.0544199624634
        Para N= 2 en resultado es: 306.8199344959197
        Para N= 3 en resultado es: 317.26415173382895
        Para N= 4 en resultado es: 317.34539033415786
        Para N= 5 en resultado es: 317.34422672196945
        Para N= 6 en resultado es: 317.3442468899962
        Para N= 7 en resultado es: 317.3442466722262
        Para N= 8 en resultado es: 317.3442466738354
        Para N= 9 en resultado es: 317.34424667382626
        Para N= 10 en resultado es: 317.3442466738264
    """
    x, w = gaussxw(N)
    x_a, w_b = gaussxwab(a, b, x, w)

    return np.sum(w_b * f(x_a))
print(f"{"-" * 50}")
print(f"Integral evaluada por método de cuadratura gaussiana.")
for i in range(10):
   resultado = integrarGaussiana(f, 1 , 3, i + 1)
   print(f"Para N= {i + 1} en resultado es: {resultado}")
print(f"{"-" * 50}")
print(f"Conclusión importante: Desde N = 5 el resultado casi no cambia, de N= 4 a N=5 cambia minúsculamente. N = 3 representa ya una aproximación aceptable.")
print(f"{"-" * 50}")