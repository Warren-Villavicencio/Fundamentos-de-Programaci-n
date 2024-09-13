weight = 85
height = 1.85

weight = float(input("Ingrese su peso: "))
height = float(input("Ingrese su Altura: "))

bmi = weight / (height ** 2)



if bmi < 18.5:
    print("Bajo de peso")
elif bmi >= 18.5:
     print("Peso normal")
elif bmi <= 24.9:
     print("Peso normal.")
     
else:
    print("sobre peso")    