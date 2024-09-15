edad = int(input(" Ingresa a tu edad: "))
anos_cotizados = int(input(" Ingresa tus años de aportación: "))

if (edad >= 60 and edad <= 65) or (edad >= 55 and anos_cotizados > 30):
    print("Puedes jubilarte.")
else:
    print("Aún no puedes jubilarte.")