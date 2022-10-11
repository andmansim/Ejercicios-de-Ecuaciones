import matplotlib as plt
import sympy
class Calcular:
    def getter(x, y, f):
        
        sympy.Eq(y(x).diff(x), f)

        # Resolviendo la ecuación
        solucion = sympy.dsolve(y(x).diff(x) - f)
        return solucion

x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = ((y(x))*x**2 - (y(x))/((y(x)) + 1))
calcular = Calcular()
solucion = calcular.getter(x, y, f)
print(solucion)