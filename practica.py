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

