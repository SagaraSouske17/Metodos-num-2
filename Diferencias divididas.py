from sympy import *

x, y = symbols('x y')

def coeficientes(tabla, grado):
  for j in range(grado):
    for i in range(grado-j):
      tabla[i].append((tabla[i+1][j+1] - tabla[i][j+1]) / (tabla[j+i+1][0] - tabla[i][0]))
  coeficientes = tabla[0][1:]
  
  return coeficientes

def polinomio_diferencias_divididas(tabla, grado):
  a = coeficientes(tabla, grado)
  polinomio = 0.0
  for j in range(grado+1):
    termino = 1
    for i in range(j):
      termino = termino * (x - tabla[i][0])
    termino = termino * a[j]
    polinomio = polinomio + termino

  return polinomio.expand()

'''
datos_ejemplo = [[1.73, 8.1], [1.82, 8.3], [2.61, 7.8], [5.22, 2.4], [8.26, -1.7]]

polinomio_ejemplo = polinomio_diferencias_divididas(datos_ejemplo, 4)
print("El polinomio de grado 4 es:\n", polinomio_ejemplo)
print("Evaluado en el punto 2.5 es:", polinomio_ejemplo.subs({x:2.5}))
'''
datos = [[2016, 14.026], [2018, 17.486], [2019, 17.424], [2020, 10.327], [2022, 7.934]]

polinomio1 = polinomio_diferencias_divididas(datos, 2)
print("\nEl polinomio de grado 2 es:\n", polinomio1)
print("Evaluado en el valor 2017 es:", polinomio1.subs({x:2017}))
g1 = plot(polinomio1, (x, 2016, 2022), show=False)
g1.title = 'Gráfica de la función:'+ str(polinomio1)
g1.xlabel = 'x'
g1.ylabel = 'f(x)'
g1.show()

polinomio2 = polinomio_diferencias_divididas(datos, 2)
print("\nEl polinomio de grado 2 es:\n", polinomio2)
print("Evaluado en el valor 2021 es:", polinomio2.subs({x:2021}))

polinomio3 = polinomio_diferencias_divididas(datos, 3)
print("\nEl polinomio de grado 3 es:\n", polinomio3)
print("Evaluado en el valor 2017 es:", polinomio3.subs({x:2017}))
g2 = plot(polinomio3, (x, 2016, 2022), show=False)
g2.title = 'Gráfica de la función:'+ str(polinomio3)
g2.xlabel = 'x'
g2.ylabel = 'f(x)'
g2.show()

polinomio4 = polinomio_diferencias_divididas(datos, 3)
print("\nEl polinomio de grado 3 es:\n", polinomio4)
print("Evaluado en el valor 2021 es:", polinomio4.subs({x:2021}))
