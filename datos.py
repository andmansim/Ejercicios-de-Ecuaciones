import matplotlib as plt
import sympy

class Calcular:
    def inicio(self, x, y, f, cond_inicial):
        #diff para el diferencial
        ec = sympy.Eq(y(x).diff(x), f)
        # Resolviendo la ecuación
        solucion = sympy.dsolve(y(x).diff(x) - f)

        print(solucion)
        if cond_inicial == True:
            # Condición inicial
            ics = {y(sympy.pi/2): sympy.exp}

            #sustituimos la condición inicial
            C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(ics), solucion.rhs.subs(x, 0))
            print(C_eq)
            #Nos saca la C
            c = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista

            print(c)
            solucion_p = sympy.Eq(y(x), sympy.exp(sympy.exp((c*sympy.tan(x/2) - c + 2)/(sympy.tan(x/2) - 1))))
            return solucion_p
        else: 
            return solucion
    
