
def main():
    # height = float(input("Height (m): "))
    # weight = float(input("Weight (kg): "))
    height = get_valid_number("Height (m): ", 0, 2)
    weight = get_valid_number("Weight (kg): ", 0, 200)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi}, which is considered {category}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
   
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def run_tests():
    bmi = calculate_bmi(4, 80)
    print(bmi)  # This  should be 20
    bmi = calculate_bmi(3.5, 200)
    print(bmi)  # This should be 81.63

    print(determine_weight_category(18))  # This should be underweight
    print(determine_weight_category(35))  # This should be overweight

    height = get_valid_number("Height (m): ", 0, 2)
    print(height)
    weight = get_valid_number("Weight (kg): ", 0, 200)
    print(weight)
