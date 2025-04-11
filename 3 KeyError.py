
registro = { "nombre": "Jose", "edad": 32,"ciudad": "Tres de Febrero"}

clave = "apellido"

try:
    valor = registro[clave]
    print(f"El'{clave}' encontrado es: {valor}")
except KeyError:
    print(f"No se puede acceder al registro: la clave '{clave}' no existe en el diccionario.")