print("Calculadora insana")
n1 = int(input("Ingrese valor 1: "))
n2 = int(input("Ingrese valor 2: "))
operacion = input("Eligue +, -, *, /: ")

if operacion == "+":
    resultado = n1 + n2
    print("El resultado de la suma Insana es:", resultado)
elif operacion == "-":
    resultado = n1 - n2
    print("El resultado de la resta Insana es:", resultado)
elif operacion == "*":
    resultado = n1 * n2
    print("El resultado de la multiplicación Insana es:", resultado)
elif operacion == "/":
    if n2 != 0:
        resultado = n1 / n2
        print("El resultado de la división Insana es:", resultado)
    else:
        print("Error: no puedes dividir 0 naranjas con 0 amigos!")
else:
    print("Error: operación no válida. Intente de nuevo!")