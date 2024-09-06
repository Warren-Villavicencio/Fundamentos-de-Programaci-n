def get_height():
    """Prompt the user to input their height."""
    return float(input("Welcome to the Rollercoaster! Before you go in, please state your height: "))

def check_height(height):
    """Check if the person meets the height requirement."""
    if height >= 120:
        print("Welcome to the Rollercoaster!")
    else:
        print("Sorry, you cannot enter.")

def main():
    """Main function to run the rollercoaster height check."""
    height = get_height()
    check_height(height)

if __name__ == "__main__":
    main()
