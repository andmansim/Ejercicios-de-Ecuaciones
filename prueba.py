import matplotlib as plt
import sympy

class Calcular:
    def inicio(self, x, y, f):
        #diff para el diferencial
        ec = sympy.Eq(y(x).diff(x), f)
        # Resolviendo la ecuación
        solucion = sympy.dsolve(y(x).diff(x) - f)

        print(solucion)

        # Condición inicial
        ics = {y(sympy.pi/2): sympy.exp}

        #sustituimos la condición inicial
        C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(ics), solucion.rhs.subs(x, 0))
        print(C_eq)
        #Nos saca la C
        c = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista

        print(c)
                
                
# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = y(x).diff(x) * sympy.sin(x) - (y(x) *sympy.log(y(x)))

ca = Calcular()
ca.inicio(x, y, f)

