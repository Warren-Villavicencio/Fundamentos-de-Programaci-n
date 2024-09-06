# Operadores de cálculo en Python

# Suma (+)
a = 5 + 3  # a = 8

# Resta (-)
b = 10 - 4  # b = 6

# Multiplicación (*)
c = 3 * 4  # c = 12

# División (/)
d = 15 / 3  # d = 5.0 (siempre devuelve un float)

# División entera (//)
e = 17 // 3  # e = 5 (descarta la parte decimal)

# Módulo (%)
f = 17 % 3  # f = 2 (resto de la división)

# Exponenciación (**)
g = 2 ** 3  # g = 8

# Operadores de asignación en Python

# Asignación simple (=)
x = 10

# Asignación con suma (+=)
x += 5  # Equivalente a: x = x + 5

# Asignación con resta (-=)
x -= 3  # Equivalente a: x = x - 3

# Asignación con multiplicación (*=)
x *= 2  # Equivalente a: x = x * 2

# Asignación con división (/=)
x /= 4  # Equivalente a: x = x / 4

# Asignación con división entera (//=)
x //= 3  # Equivalente a: x = x // 3

# Asignación con módulo (%=)
x %= 3  # Equivalente a: x = x % 3

# Asignación con exponenciación (**=)
x **= 2  # Equivalente a: x = x ** 2

# Ejemplo de uso
def ejemplo_python():
    numero = 10
    print(f"Número inicial: {numero}")
    
    numero += 5
    print(f"Después de suma: {numero}")
    
    numero *= 2
    print(f"Después de multiplicación: {numero}")
    
    numero %= 7
    print(f"Después de módulo: {numero}")

ejemplo_python()
