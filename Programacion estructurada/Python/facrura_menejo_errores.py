import logging

# Configuración del registro de errores
logging.basicConfig(filename='errores.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

class FacturaError(Exception):
    """Clase base para excepciones en este módulo."""
    pass

class ValorFacturaError(FacturaError):
    """Excepción lanzada por un valor de factura inválido."""
    pass

class NumeroComensalesError(FacturaError):
    """Excepción lanzada por un número de comensales inválido."""
    pass

def obtener_valor_factura():
    while True:
        try:
            factura_restaurante = float(input("Ingrese el valor total de la factura: "))
            if factura_restaurante <= 0:
                raise ValorFacturaError("El valor de la factura debe ser mayor que cero.")
            return factura_restaurante
        except ValueError:
            print("Entrada no válida: Debe ingresar un número.")
        except ValorFacturaError as e:
            print(f"Entrada no válida: {e}")
            logging.error(e)

def obtener_numero_comensales():
    while True:
        try:
            comensales = int(input("Ingrese el número de comensales: "))
            if comensales <= 0:
                raise NumeroComensalesError("El número de comensales debe ser mayor que cero.")
            return comensales
        except ValueError:
            print("Entrada no válida: Debe ingresar un número entero.")
        except NumeroComensalesError as e:
            print(f"Entrada no válida: {e}")
            logging.error(e)

def calcular_division_factura(factura_restaurante, comensales):
    try:
        dividir_factura = factura_restaurante / comensales
        return round(dividir_factura, 2)
    except ZeroDivisionError as e:
        print("Error: El número de comensales no puede ser cero.")
        logging.error(e)
        return None

def main():
    factura_restaurante = obtener_valor_factura()
    comensales = obtener_numero_comensales()
    dividir_factura = calcular_division_factura(factura_restaurante, comensales)
    
    if dividir_factura is not None:
        print(f"A los {comensales} les tocará pagar a cada uno el valor de: {dividir_factura}")

if __name__ == "__main__":
    main()
