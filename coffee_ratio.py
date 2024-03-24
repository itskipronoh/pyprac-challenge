def determine_coffee_style(ratio):
    
    if ratio <= 1:
        return "ristretto"
    elif 1 < ratio <= 2:
        return "normale"
    elif 2 < ratio <= 3:
        return "lungo"
    else:
        return "lungo"


def check_coffee():

    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


def get_valid_number(prompt, max_value):
   
    while True:
        try:
            value = float(input(prompt))
            if 0 < value <= max_value:
                return value
            else:
                print(f"Please enter a positive number less than or equal to {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to Coffee Style Determiner!")
    print("Let's determine the style of your coffee based on the brew ratio.")

    dose = get_valid_number("Enter the dose (grams): ", 100)
    yield_ = get_valid_number("Enter the yield (grams): ", 100)

    ratio = yield_ / dose
    print(f"\n{dose}:{yield_} is considered {determine_coffee_style(ratio)}")


if __name__ == "__main__":
    main()
