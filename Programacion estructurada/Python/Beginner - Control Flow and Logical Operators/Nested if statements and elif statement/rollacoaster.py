print (" Welcome to roll copster")

height = int(input(" Ingresa a tu altura:"))


if height >= 120:
    #mayor que 120
    print(" Puedes ingresar")
    age = int(input(" ¿Cuál es tu edad: "))
    if age <= 12:
        print(" Pagarás 5 dólares.")
        # menor que 12
    elif age <= 18:
    
        print(" Pagarás 7 dólares.")
    else:
        
        print(" Pagarás 12 dólares.")
        
else:

    print(" No puedes ingresar.")
    
    