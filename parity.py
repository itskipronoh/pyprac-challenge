def print_parity(number):
   
    parity = number % 2
    print(f"Parity of {number} should be {parity}:")


def test_print_parity():
    print_parity(4)
    print_parity(41)


def calculate_parity(number):
    
    return number % 2


def test_calculate_parity():
    print(f"Parity of 4 should be 0:", calculate_parity(4))
    print(f"Parity of 41 should be 1:", calculate_parity(41))


def is_odd(number):
  
    return number % 2 != 0


def test_is_odd():
    print(f"Is 4 odd? Expected: False, Actual:", is_odd(4))
    print(f"Is 41 odd? Expected: True, Actual:", is_odd(41))


def main():
    print("Testing print_parity:")
    test_print_parity()

    print("\nTesting calculate_parity:")
    test_calculate_parity()

    print("\nTesting is_odd:")
    test_is_odd()


if __name__ == "__main__":
    main()
