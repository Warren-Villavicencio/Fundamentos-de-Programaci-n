print("Do the lamps work?")

lampara_conectada = str(input(" La lámpara está conectada: "))



if lampara_conectada == True:
     print(" La lámpara está conectada" )
     lampara_encendida = input(" La lámpara está encendida: ")
     if lampara_encendida == False:
       print(" La lámpara prendió correctamente." )
     else:
       print(" Hay que cambiar el foco de la lámpara." )
                
else:
     
    print(" Hay que conectar la lámpara al tomacorriente." )
    
    if lampara_encendida == False:
       print(" La lámpara prendió correctamente." )
    else:
       print(" Hay que cambiar el foco de la lámpara." )