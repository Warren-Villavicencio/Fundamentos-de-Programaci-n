def get_pizza_size():
    size = str(input("What size pizza do you want S, M or L: ")).lower()
    if size not in ["s", "m", "l"]:
        print("Debes elegir entre S, M o L")
        exit()
    return size

def get_pepperoni_choice():
    choice = str(input("Do you want pepperoni in your Pizza (yes or no): ")).lower()
    if choice not in ["yes", "no"]:
        print("Respuesta inválida para pepperoni. Debes elegir entre 'yes' o 'no'")
        exit()
    return choice

def get_cheese_choice():
    choice = str(input("Do you want extra cheese (yes or no): ")).lower()
    if choice not in ["yes", "no"]:
        print("Respuesta inválida para queso extra. Debes elegir entre 'yes' o 'no'")
        exit()
    return choice

def calculate_price(size, add_pepperoni, add_extra_cheese):
    prices = {"s": 5, "m": 9, "l": 15}
    pagaras = prices[size]
    if add_pepperoni == "yes":
        pagaras += 2 if size == "m" else 3
    if add_extra_cheese == "yes":
        pagaras += 1
    return pagaras
