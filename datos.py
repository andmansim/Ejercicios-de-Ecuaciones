import matplotlib as plt
import sympy
class Calcular:
    def __init__(self, x, y, f):

        #diff para el diferencial
        ec = sympy.Eq(y(x).diff(x), f)

'''
La ecuación es Eq(Derivative(y(x), x), -3*x**2*y(x) + 6*x**2)
'''


# Resolviendo la ecuación
solucion = sympy.dsolve(y(x).diff(x) - f)

'''
la solución de la ec es Eq(y(x), C1*exp(-x**3) + 2)
'''


# Condición inicial
ics = {y(0): 2}

#sustituimos la condición inicial
C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(ics), solucion.rhs.subs(x, 0))

'''
Con la condición inicial es Eq(2, C1 + 2)
'''


#Nos saca la C
c = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista

'''
El valor de la C es 0
'''


#Solución particular
'''
Hay q poner la solución que nos sale y cambiar la C1 por c
Poner sympy. y la operación, en este caso es exp pq es la exponencial
'''
solucion_p = sympy.Eq(y(x), c* sympy.exp(-x**3) + 2)

'''
Solución particuar : Eq(y(x), 2)
'''