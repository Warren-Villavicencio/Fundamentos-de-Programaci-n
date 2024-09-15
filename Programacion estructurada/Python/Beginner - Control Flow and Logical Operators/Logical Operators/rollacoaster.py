print (" Welcome to roll copster")

height = int(input(" Ingresa a tu altura:"))


if height >= 120:
    #mayor que 120
    print(" Puedes ingresar")
    age = int(input(" ¿Cuál es tu edad: "))
    if age <= 12:
        pagaras = 5
        print(" Pagarás 5 dólares.")
        # menor que 12
    elif age <= 18:
        pagaras = 7
        print(" Pagarás 7 dólares.")
    else:
        pagaras = 12
        print(" Pagarás 12 dólares.")
        
        want_phot = str(input(" Si tú quieres una foto di si o no: "))
        
        if want_phot == "si":
            pagaras += 3
            print(f" Tu precio final es: {pagaras}")
            
        
else:

    print(" No puedes ingresar.")
    
    