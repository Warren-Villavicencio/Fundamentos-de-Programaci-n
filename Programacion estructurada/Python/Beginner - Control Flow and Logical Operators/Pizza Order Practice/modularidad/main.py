from funciones import get_pizza_size
from funciones import get_pepperoni_choice
from funciones import get_cheese_choice
from funciones import calculate_price

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
