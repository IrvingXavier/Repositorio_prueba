def solicitar_num(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: El dato ingresado no es un número.")

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Salir")
    print("-------------------")

def calcular(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return a / b
    else:
        raise ValueError("Operación no válida.")

def solicitar_num(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: El dato ingresado no es un número.")

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Salir")
    print("-------------------")

def calcular(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return a / b
    else:
        raise ValueError("Operación no válida.")

# Función principal para ejecutar la calculadora
def main():
    operaciones = {1: '+', 2: '-', 3: '*', 4: '/'}
    
    while True:
        mostrar_menu()
        opcion = int(solicitar_num("Elige una opción (1-5): "))
        
        if opcion == 5:
            print("¡Hasta luego!")
            break
            
        if opcion in operaciones:
            num1 = solicitar_num("Ingresa el primer número: ")
            num2 = solicitar_num("Ingresa el segundo número: ")
            op = operaciones[opcion]
            
            try:
                resultado = calcular(num1, num2, op)
                print(f"Resultado: {resultado}")
            except (ZeroDivisionError, ValueError) as e:
                print(f"Error: {e}")
        else:
            print("Opción no válida. Elige del 1 al 5.")

if __name__ == "__main__":
    main()
