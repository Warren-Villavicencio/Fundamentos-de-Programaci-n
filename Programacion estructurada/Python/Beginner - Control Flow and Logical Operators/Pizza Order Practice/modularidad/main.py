try:
    from funciones import get_pizza_size, get_pepperoni_choice, get_cheese_choice, calculate_price

    # Programa principal
    print("Welcome to pizza order Delivery")

    # Obtener el tamaño de la pizza
    size = get_pizza_size()

    # Obtener la elección de pepperoni
    add_pepperoni = get_pepperoni_choice()

    # Obtener la elección de queso extra
    add_extra_cheese = get_cheese_choice()

    # Calcular el precio final
    pagaras = calculate_price(size, add_pepperoni, add_extra_cheese)

    # Mostrar el precio final
    print(f"Tu precio final es: {pagaras}")

except ImportError as e:
    print(f"Error al importar: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
