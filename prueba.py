import matplotlib as plt
import sympy

class Calcular:
    def __init__(self, x, y, f):
        
        sympy.Eq(y(x).diff(x), f)

    
    def getter(self):
        # Resolviendo la ecuación
        solucion = sympy.dsolve(f)
        return solucion[1]

x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = y(x).diff(x)  - (y(x) *sympy.log(y(x)))/sympy.sin(x)
calcular = Calcular(x, y, f)
solucion = calcular.getter()
print(solucion)
