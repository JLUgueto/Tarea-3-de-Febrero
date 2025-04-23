def calcular_promedio(*args):

    promedio = sum(args) / len(args) if len(args) > 0 else 0
    print(f"El promedio es: {promedio}")


entrada = input("Ingrese los números separados por coma: ")


numeros = [float(n.strip()) for n in entrada.split(",")]


calcular_promedio(*numeros)