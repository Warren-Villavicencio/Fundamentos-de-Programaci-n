import funciones from funciones

# Main program
print("Welcome to pizza order Delivery")
size = get_pizza_size()
add_pepperoni = get_pepperoni_choice()
add_extra_cheese = get_cheese_choice()
pagaras = calculate_price(size, add_pepperoni, add_extra_cheese)
print(f"Tu precio final es: {pagaras}")
