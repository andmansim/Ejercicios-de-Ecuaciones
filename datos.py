import matplotlib as plt
import sympy
class Calcular:

    def getter(self, x, y, f):
        sympy.Eq(y(x).diff(x), f)
        # Resolviendo la ecuación
        solucion = sympy.dsolve(f)
        return solucion


    
