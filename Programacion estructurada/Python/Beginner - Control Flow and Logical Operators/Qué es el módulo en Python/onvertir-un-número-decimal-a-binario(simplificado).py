numero_decimal = 13
while numero_decimal > 0:
    residuo = numero_decimal % 2
    print(residuo, end='')
    numero_decimal //= 2  # División entera para obtener el cociente