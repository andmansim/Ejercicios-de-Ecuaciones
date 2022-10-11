import helpers
import datos
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
            f = 6*x**2 - 3*x**2*(y(x))
            
                
        if opcion == '2':
            print("Halla la solución particular de la ecuación y' senx= y Ln y que satisfaga la condición inicial\n")
            print(" y(pi/2) = e")
        
        if opcion == '3':
            print("Resuelve  la siguiente ecuación diferencial\n")
            print("y' - y / (t-2)  = 2(t-2)^2")
        
        if opcion == '4':
            print("Resuelve la siguiente ecuación diferencial y representa la familia de soluciones\n")
            print("2ty' - y = 3t^2 ")
            
                
        
        if opcion == '5':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")