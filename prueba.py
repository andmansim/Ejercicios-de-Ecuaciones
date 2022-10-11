import matplotlib as plt
import sympy
class Calcular:
    def __init__(self, x, y, f):
        
        sympy.Eq(y(x).diff(x), f)

    @property   
    def getter(self):
        # Resolviendo la ecuación
        solucion = sympy.dsolve(y(x).diff(x) - f)
        return solucion

x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = ((y(x))*x**2 - (y(x))/((y(x)) + 1))
calcular = Calcular(x, y, f)
solucion = calcular.getter()
print(solucion)