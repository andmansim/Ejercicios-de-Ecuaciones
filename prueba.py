import matplotlib as plt
import sympy

class Calcular:
    def __init__(self, x, y, f):
        
        sympy.Eq(y(x).diff(x), f)

    
    def getter(self):
        # Resolviendo la ecuación
        solucion = sympy.dsolve(f)
        return solucion
    
    def condicion_inicial(self, c):
     
        
        C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(c), solucion.rhs.subs(x, 0))


        print(C_eq)

        #Nos saca la C
        ci = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista
        print(ci)

        #Solución particular

        solucion_p = sympy.Eq(y(x), sympy.exp(ci*sympy.sqrt(sympy.cos(x) - 1)/sympy.sqrt(sympy.cos(x) + 1)))
        return solucion_p

x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = y(x).diff(x)  - (y(x) *sympy.log(y(x)))/sympy.sin(x)
calcular = Calcular(x, y, f)
solucion = calcular.getter()
print(solucion)
ics = {y(sympy.pi/2): sympy.exp}
print(ics)

 
C_eq = sympy.Eq(solucion.lhs.subs(x, 0).subs(ics), solucion.rhs.subs(x, 0))


print(C_eq)

#Nos saca la C
ci = sympy.solve(C_eq)[0] #Con [0] pq nos lo da en una lista
print(ci)

#Solución particular

solucion_p = sympy.Eq(y(x), sympy.exp(ci*sympy.sqrt(sympy.cos(x) - 1)/sympy.sqrt(sympy.cos(x) + 1)))