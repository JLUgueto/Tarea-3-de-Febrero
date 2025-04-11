a = int(input("Introduce un número entero: "))
b = int(input("Introduce un número entero: "))

try:
    resultado = a / b
    
    print(resultado)

except ZeroDivisionError:
    print(f"Ha ocurrido un error. No se puede dividir por 0")
