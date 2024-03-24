import random

def jcu_grade(score):
   
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


def test_jcu_grade():
   
    print("Testing JCU Grades:")
    print("50 ->", jcu_grade(50))  # Expected: P
    print("64 ->", jcu_grade(64))  # Expected: P
    print("65 ->", jcu_grade(65))  # Expected: C
    print("74 ->", jcu_grade(74))  # Expected: C
    print("75 ->", jcu_grade(75))  # Expected: D
    print("84 ->", jcu_grade(84))  # Expected: D
    print("85 ->", jcu_grade(85))  # Expected: HD
    print("89 ->", jcu_grade(89))  # Expected: HD


def main():
    while True:
        score = float(input("Enter the subject total score (negative number to exit): "))
        if score < 0:
            break
        grade = jcu_grade(score)
        print(f"The score {score} is {grade}")

    num_random_scores = int(input("How many random scores: "))
    for _ in range(num_random_scores):
        random_score = random.randint(0, 100)
        grade = jcu_grade(random_score)
        print(f"{random_score} = {grade}")


if __name__ == "__main__":
    test_jcu_grade()
    main()
