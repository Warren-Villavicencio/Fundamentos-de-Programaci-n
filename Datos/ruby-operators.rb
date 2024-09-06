# Operadores de cálculo en Ruby

# Suma (+)
a = 5 + 3  # a = 8

# Resta (-)
b = 10 - 4  # b = 6

# Multiplicación (*)
c = 3 * 4  # c = 12

# División (/)
d = 15.0 / 3  # d = 5.0

# División entera (//)
e = 17 / 3  # e = 5

# Módulo (%)
f = 17 % 3  # f = 2 (resto de la división)

# Exponenciación (**)
g = 2 ** 3  # g = 8

# Operadores de asignación en Ruby

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

# Asignación con módulo (%=)
x %= 3  # Equivalente a: x = x % 3

# Asignación con exponenciación (**=)
x **= 2  # Equivalente a: x = x ** 2

# Operadores de comparación
a = 5
b = 10
puts a == b  # false (igualdad)
puts a != b  # true (desigualdad)
puts a > b   # false (mayor que)
puts a < b   # true (menor que)
puts a >= b  # false (mayor o igual que)
puts a <= b  # true (menor o igual que)

# Operador de rango
rango = 1..5  # Incluye 5
rango = 1...5 # Excluye 5

# Ejemplo de uso
def ejemplo_ruby
  numero = 10
  puts "Número inicial: #{numero}"
  
  numero += 5
  puts "Después de suma: #{numero}"
  
  numero *= 2
  puts "Después de multiplicación: #{numero}"
  
  numero %= 7
  puts "Después de módulo: #{numero}"
end

ejemplo_ruby
