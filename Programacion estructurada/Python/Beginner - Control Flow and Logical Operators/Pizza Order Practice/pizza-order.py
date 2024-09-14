print(" Welcome to pizza order Delivery")

size = str(input(" What size pizza do you want S, M or L: "))

add_peperroni = str(input("  Do you want pepperoni in your Pizza:  "))

add_extra_chesse = str(input(" Do you want extra cheese. "))

if size == "s":
    pagaras = 5
    
elif size == "m":
     pagaras = 9
     
elif size == "l":
      pagaras = 15
      
else:

    print(" Debes elegir entre m s l")
           
      
if add_peperroni == "si":
    if size == "m":
       pagaras += 2
    else:
          pagaras += 3
    
if add_extra_chesse == "si":
    pagaras += 1
    print(f" Tu precio final es: {pagaras}")
      

      
    
    

