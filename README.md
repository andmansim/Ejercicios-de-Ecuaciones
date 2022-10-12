# -Ejercicios-de-Ecuaciones

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/-Ejercicios-de-Ecuaciones.git)
https://github.com/andmansim/-Ejercicios-de-Ecuaciones.git

He resuelto una serie de ejercicio de ecuaciones diferenciales.
El código es:
# Run
```
import menu
if __name__ == '__main__':
    menu.iniciar()
```
# Menu
```
import helpers
import datos as d
import sympy
def iniciar():
     while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejericio 1 ")
        print("[2] Ejericio 2 ")
        print("[3] Ejericio 3 ")
        print("[4] Ejericio 4 ")
        print("[5] Cerrar el Manager ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Resuelve la siguiente ecuación diferencial y obtén la constante usando la condición inicial \n")
            print("y' = (x^2 y - y)/(y + 1)  , y(3) = -1")
            # Defino incognitas
            x = sympy.symbols('x')
            y = sympy.Function('y')

            # Defino la función
            f = (y(x)*x**2 - y(x))/(y(x) + 1)            
            
            ics = {y(0): 2}
            ca = d.Calcular()
            c, solucion = ca.inicio(x, y, f, True, 1, ics)
            print('La solución es:')
            print(solucion)
            print('La solucion particular es: ' + str(c))
                
        if opcion == '2':
            print("Halla la solución particular de la ecuación y' senx= y Ln y que satisfaga la condición inicial\n")
            print(" y(pi/2) = e")

            # Defino incognitas
            x = sympy.symbols('x')
            y = sympy.Function('y')

            # Defino la función
            f = y(x).diff(x) * sympy.sin(x) - (y(x) *sympy.log(y(x)))

            ca = d.Calcular()
            ics = {y(sympy.pi/2): sympy.exp}
            c, solucion = ca.inicio(x, y, f, True, 2, ics)
            print('La solucion particular es: ' + str(c))
        
        if opcion == '3':
            print("Resuelve  la siguiente ecuación diferencial\n")
            print("y' - y / (t-2)  = 2(t-2)^2")
            # Defino incognitas
            t = sympy.symbols('t')
            y = sympy.Function('y')

            # Defino la función
            f = (y(t).diff(t) - y(t))/ (t - 2) -2*(t-2)**2
            ca = d.Calcular()
            solucion = ca.inicio(t, y, f, False, 0, 0)
            print('La solucion es: ' + str(solucion))
            
        if opcion == '4':
            print("Resuelve la siguiente ecuación diferencial y representa la familia de soluciones\n")
            print("2ty' - y = 3t^2 ")
            # Defino incognitas
            t = sympy.symbols('t')
            y = sympy.Function('y')

            # Defino la función
            f = (y(t).diff(t)*2*t - y(t) -3*t**2)
            ca = d.Calcular()
            ics = {y(sympy.pi/2): sympy.exp}
            solucion = ca.inicio(t, y, f, False, 0, 0)
            print('La solucion particular es: ' + str(solucion))

        
        if opcion == '5':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")
```
# Helpers
```
import os
import re #para comprobar si lo que nos dan está bien
import platform #detecta el sistema operativo que queremos y lo adapta para poder trabajar con él.

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
```

# Datos 
```
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
```
