import operator

# Operaciones aritméticas
a = 5
b = 3
print(operator.add(a, b))   # Suma: 8
print(operator.sub(a, b))   # Resta: 2
print(operator.mul(a, b))   # Multiplicación: 15

# Comparaciones
print(operator.eq(a, b))   # Igualdad: False
print(operator.gt(a, b))   # Mayor que: True

# Uso con listas
lista = [2, 5, 1, 4]
print(sorted(lista, key=operator.itemgetter(1)))  # Ordenar por el segundo elemento

# Uso con tuplas
tupla = (("a", 2), ("b", 1), ("c", 3))
print(sorted(tupla, key=operator.itemgetter(1)))  # Ordenar por el segundo elemento de cada tupla

# Uso con objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = [
    Persona("Ana", 30),
    Persona("Juan", 25),
    Persona("Pedro", 32)
]
print(sorted(personas, key=operator.attrgetter('edad')))  # Ordenar por edad