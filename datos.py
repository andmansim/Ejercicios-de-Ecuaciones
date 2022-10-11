import matplotlib as plt
import sympy
class Calcular:
    
    '''   def __init__(self, x, y, f):
        
        sympy.Eq(y(x).diff(x), f)
'''
    
    def getter(self, x, y, f):
        sympy.Eq(y(x).diff(x), f)
        # Resolviendo la ecuación
        solucion = sympy.dsolve(f)
        return solucion


    '''def condicion_inicial(self, c):
 
        #sustituimos la condición inicial
        C_eq = sympy.Eq(solucion.lhs.subs(self.x, 0).subs(c), solucion.rhs.subs(self.x, 0))

        #Nos saca la C
        c1 = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista
        return c1'''


