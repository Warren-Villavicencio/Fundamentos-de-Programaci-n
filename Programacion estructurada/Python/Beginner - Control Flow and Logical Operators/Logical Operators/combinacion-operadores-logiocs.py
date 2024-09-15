# Ejemplo: Verificando si un año es bisiesto
# Combinación de operadores 'and' y 'not'

año = 2024
# Un año es bisiesto si es divisible por 4, pero no por 100, a menos que sea divisible por 400
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")