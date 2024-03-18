from sympy import *

x, y = symbols('x y')

def productosL(t, k, longitud):
  numerador = 1.0
  denominador = 1.0

  for i in range(longitud):
    if i != k:
      numerador = numerador * (x - t[i][0])
      denominador = denominador * (t[k][0] - t[i][0])

  return simplify(numerador/denominador).expand()

def sumaL(t, longitud):
  polinomio = 0.0

  for i in range(longitud):
    polinomio = polinomio + productosL(t, i, longitud) * t[i][1]

  return polinomio


#datos_ejemplo = [[1.73, 8.1], [1.82, 8.3], [2.61, 7.8]]
puntos_para_P2_2017 = [[2016, 14.026], [2018, 17.486], [2019, 17.424]]
puntos_para_P2_2021 = [[2019, 17.424], [2020, 10.327], [2022, 7.934]]
puntos_para_P3_2017 = [[2016, 14.026], [2018, 17.486], [2019, 17.424], [2020, 10.327]]
puntos_para_P3_2021 = [[2018, 17.486], [2019, 17.424], [2020, 10.327], [2022, 7.934]]

lagrange1 =  sumaL(puntos_para_P2_2017, len(puntos_para_P2_2017))
print("\nLos puntos usados para conseguir el polinimo son:\n")
pprint(Matrix(puntos_para_P2_2017))
print("\nEl polinomio de Lagrange de segundo grado que se ajusta a esos puntos es:\n", lagrange1)
print("Evaluando en 2017 da como resultado", lagrange1.subs({x:2017}))
graf1 = plot(lagrange1, (x, 2016, 2022), show=False)
graf1.title = 'Gráfica de la función:'+ str(lagrange1)
graf1.xlabel = 'x'
graf1.ylabel = 'f(x)'
graf1.show()

lagrange2 =  sumaL(puntos_para_P2_2021, len(puntos_para_P2_2021))
print("\nLos puntos usados para conseguir el polinimo son:\n")
pprint(Matrix(puntos_para_P2_2021))
print("\nEl polinomio de Lagrange de segundo grado que se ajusta a esos puntos es:\n", lagrange2)
print("Evaluando en 2021 da como resultado", lagrange2.subs({x:2021}))
graf2 = plot(lagrange2, (x, 2016, 2022), show=False)
graf2.title = 'Gráfica de la función:'+ str(lagrange2)
graf2.xlabel = 'x'
graf2.ylabel = 'f(x)'
#graf2.extend(graf1)
graf2.show()

lagrange3 =  sumaL(puntos_para_P3_2017, len(puntos_para_P3_2017))
print("\nLos puntos usados para conseguir el polinimo son:\n")
pprint(Matrix(puntos_para_P3_2017))
print("\nEl polinomio de Lagrange de tercer grado que se ajusta a esos puntos es:\n", lagrange3)
print("Evaluando en 2017 da como resultado", lagrange3.subs({x:2017}))
graf3 = plot(lagrange3, (x, 2016, 2022), show=False)
graf3.title = 'Gráfica de la función:'+ str(lagrange3)
graf3.xlabel = 'x'
graf3.ylabel = 'f(x)'
graf3.show()

lagrange4 =  sumaL(puntos_para_P3_2021, len(puntos_para_P3_2021))
print("\nLos puntos usados para conseguir el polinimo son:\n")
pprint(Matrix(puntos_para_P3_2021))
print("\nEl polinomio de Lagrange de tercer grado que se ajusta a esos puntos es:\n", lagrange4)
print("Evaluando en 2021 da como resultado", lagrange4.subs({x:2021}))
coordenadas_punto4 = (2021, lagrange4.subs({x:2021}))
graf4 = plot(lagrange4, (x, 2016, 2022), show=False)
graf4.title = 'Gráfica de la función:'+ str(lagrange4)
graf4.xlabel = 'x'
graf4.ylabel = 'f(x)'
graf4.show()
