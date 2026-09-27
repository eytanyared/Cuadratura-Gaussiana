#Cuadratura Gaussiana

Este método aproxima el valor de una integral mediante una suma de la función en puntos específicos, tal que:
\[ \int_{-1}^{1} f(x) dx \approx \sum_{i=1}^{N} w_i f(x_i) \]

Donde los puntos $x_i$ son las raíces del polinomio de legendre de grado N
y los pesos $w_i$ son coeficientes derivados de los polonomios de legendre

##Casos con intervalos diferentes a [-1, 1]

Para un intervalo $[a, b]$, se aplica una transformación lineal, tal que:
\[ x(t) = \frac{b-a}{2}t + \frac{a+b}{2} \]
