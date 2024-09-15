# Archivo: filtrar_lista.py
"""
Este programa filtra los elementos pares de una lista.
"""

numeros = [1, 2, 3, 4, 5, 6]
numeros_impares = [num for num in numeros if not num % 2 == 0]

print("Números impares:", numeros_impares)