factura_restaurante = float(input(" Ingrese el valor total De la factura:"))
comensales = int(input("Ingrese el número de comensales: "))

dividir_factura = factura_restaurante / comensales

print(f" A los {comensales} les tocara pagar a cada uno el valor de: {round(dividir_factura,2)}")