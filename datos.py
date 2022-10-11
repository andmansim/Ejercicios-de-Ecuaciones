import matplotlib as plt
import sympy
class Calcular:
    def __init__(self, x, y, f):
        self.y = y
        self.x = x
        self.f = f 
        #diff para el diferencial
        ec = sympy.Eq(self.y(self.x).diff(self.x), self.f)

        # Resolviendo la ecuación
        solucion = sympy.dsolve(self.y(self.x).diff(self.x) - self.f)

    def condicion_inicial(self):
    
        # Condición inicial
        ics = {self.y(0): 2}

        #sustituimos la condición inicial
        C_eq = sympy.Eq(solucion.lhs.subs(self.x, 0).subs(ics), solucion.rhs.subs(self.x, 0))

        #Nos saca la C
        c = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista


