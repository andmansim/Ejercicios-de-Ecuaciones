import helpers
import datos as d
import sympy
import numpy as np
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
            f = y(x).diff(x) - (y(x)*x**2 - y(x))/(y(x) + 1)
            calcular = d.Calcular()
            solucion = calcular.getter(x, y, f)
            print('La solución es:')
            print(solucion[1])
            ics = {y(0): 2}
            c = calcular.condicion_inicial(ics)
            print('La C es: ' + str(c))
            
                
        if opcion == '2':
            '''Revisarrrrrrrrrrrrrrrrrrr'''
            print("Halla la solución particular de la ecuación y' senx= y Ln y que satisfaga la condición inicial\n")
            print(" y(pi/2) = e")
            # Defino incognitas
            x = sympy.symbols('x')
            y = sympy.Function('y')

            # Defino la función
            f = y(x).diff(x) * sympy.sin(x) - (y(x) *sympy.log(y(x)))
            calcular = d.Calcular()
            solucion = calcular.getter(x, y, f)
            print('La solución es:')
            print(solucion)
            ics = {y(sympy.pi/2): sympy.exp}
            c = calcular.condicion_inicial(ics)
            print('La C es: ' + str(c))
        
        if opcion == '3':
            print("Resuelve  la siguiente ecuación diferencial\n")
            print("y' - y / (t-2)  = 2(t-2)^2")
            # Defino incognitas
            t = sympy.symbols('t')
            y = sympy.Function('y')

            # Defino la función
            f = (y(t).diff(t) - y(t))/ (t - 2) -2*(t-2)**2
            calcular = d.Calcular()
            solucion = calcular.getter(t,  y, f)
            print('La solución es:')
            print(solucion)
        
        if opcion == '4':
            print("Resuelve la siguiente ecuación diferencial y representa la familia de soluciones\n")
            print("2ty' - y = 3t^2 ")
            # Defino incognitas
            t = sympy.symbols('t')
            y = sympy.Function('y')

            # Defino la función
            f = (y(t).diff(t)*2*t - y(t) -3*t**2)
            calcular = d.Calcular()
            solucion = calcular.getter(t,  y, f)
            print('La solución es:')
            print(solucion)
                
        
        if opcion == '5':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")