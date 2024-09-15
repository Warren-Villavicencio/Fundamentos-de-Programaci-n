# Archivo: validar_contrasena.py
"""
Este programa valida si una contraseña cumple ciertos criterios.
"""

contrasena = "contraseña123"  # Cambia esta contraseña para probar

# La contraseña debe tener al menos 8 caracteres y contener al menos un número
if not (len(contrasena) >= 8 and any(char.isdigit() for char in contrasena)):
    print("La contraseña no es válida")
else:
    print("La contraseña es válida")