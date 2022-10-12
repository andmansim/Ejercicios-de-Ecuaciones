import matplotlib as plt
import sympy

class Calcular:
    def inicio(self, x, y, f, cond_inicial, n, ics):
        #diff para el diferencial
        ec = sympy.Eq(y(x).diff(x), f)
        # Resolviendo la ecuación
        solucion = sympy.dsolve(y(x).diff(x) - f)

        if cond_inicial == True:
            # Condición inicial
            
            #sustituimos la condición inicial
            C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(ics), solucion.rhs.subs(x, 0))
            #Nos saca la C
            c = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista
            if n == 2:
                solucion_p = sympy.Eq(y(x), sympy.exp(sympy.exp((c*sympy.tan(x/2) - c + 2)/(sympy.tan(x/2) - 1))))
            
            elif n == 1:
                solucion_p = sympy.Eq(y(x), sympy.LambertW((c*sympy.exp(x*(x**2 - 3)))**(1/3)*(-1 - sympy.sqrt(3)*I)/2))
            return solucion_p, solucion   
        else: 
            return solucion
    
