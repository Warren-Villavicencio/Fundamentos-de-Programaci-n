print(" Welcome to the game")

election_one = str(input(" Elige la derecha o la izquierda l o r: "))
election_two = str(input(" Eligen nadar o esperar. s o w: "))
election_three = str(input(" Elige la puerta correcta. b , r o y: "))

if election_one == "r":
    print(" Game over")
elif election_one == "l":
    if election_two == "s":
       print(" Game over")
    elif election_three == "w":
        if election_three  