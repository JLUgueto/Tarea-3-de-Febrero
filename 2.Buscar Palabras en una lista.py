def buscar_palabra(palabra, *args):
   
    resultado = "La palabra fue encontrada" if palabra in args else "La palabra NO fue encontrada"
    print(resultado)


entrada = input("Ingrese una lista de palabras separadas por una coma: ")
palabras = [p.strip() for p in entrada.split(",")]

# Pedimos la palabra a buscar
buscar = input("Ingrese la palabra que desea buscar: ").strip()


buscar_palabra(buscar, *palabras)
