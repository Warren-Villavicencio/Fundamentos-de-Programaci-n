nombre_usuario = input("Ingresa tu nombre: ")
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

altura_al_cuadrado = altura * altura
indice_masa_corporal = peso / altura_al_cuadrado

print(f"{nombre_usuario}, tu índice de masa corporal es: {round(indice_masa_corporal,2)}")
