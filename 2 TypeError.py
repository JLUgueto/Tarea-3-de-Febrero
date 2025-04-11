

def sumemos(a,b):   
    try:
        resultado = a + b
        print(resultado)
    except TypeError:
        print(f"Ambos operadores deben ser numericos")
 
sumemos(20, "hola")