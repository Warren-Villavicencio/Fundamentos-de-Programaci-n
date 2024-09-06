from get_heigth import get_heigth
from check_height import check_height

def main():
    """Main function to run the rollercoaster height check."""
    height = get_height()
    check_height(height)

if __name__ == "__main__":
    main()
