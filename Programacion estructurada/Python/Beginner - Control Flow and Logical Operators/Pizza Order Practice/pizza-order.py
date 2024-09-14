# Bienvenida al usuario
print("Welcome to pizza order Delivery")

# Solicitar el tamaño de la pizza
size = str(input("What size pizza do you want S, M or L: ")).lower()

# Solicitar si desea pepperoni
add_pepperoni = str(input("Do you want pepperoni in your Pizza (yes or no): ")).lower()

# Solicitar si desea queso extra
add_extra_cheese = str(input("Do you want extra cheese (yes or no): ")).lower()

# Inicializar la variable para el precio final
pagaras = 0

# Validar el tamaño de la pizza
if size == "s":
    pagaras = 5
elif size == "m":
    pagaras = 9
elif size == "l":
    pagaras = 15
else:
    print("Debes elegir entre S, M o L")
    exit()  # Salir del programa si el tamaño no es válido

# Validar si desea pepperoni
if add_pepperoni == "yes":
    if size == "m":
        pagaras += 2
    else:
        pagaras += 3
elif add_pepperoni != "no":
    print("Respuesta inválida para pepperoni. Debes elegir entre 'yes' o 'no'")
    exit()  # Salir del programa si la respuesta no es válida

# Validar si desea queso extra
if add_extra_cheese == "yes":
    pagaras += 1
elif add_extra_cheese != "no":
    print("Respuesta inválida para queso extra. Debes elegir entre 'yes' o 'no'")
    exit()  # Salir del programa si la respuesta no es válida

# Mostrar el precio final
print(f"Tu precio final es: {pagaras}")
