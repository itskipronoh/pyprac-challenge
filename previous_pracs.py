
#Calculate salary for worker level

def calculate_salary(worker_level):
 
    if worker_level == 1:
        return 50000
    elif worker_level == 2:
        return 60000
    elif worker_level == 3:
        return 70000
    else:
        return 0


def main():
    print("Salary Calculator")

    try:
        worker_level = int(input("Enter worker's level (1, 2, or 3): "))
        if worker_level < 1 or worker_level > 3:
            raise ValueError("Worker level should be 1, 2, or 3")
    except ValueError as e:
        print("Invalid input. Please enter a valid worker level.")
        return

    salary = calculate_salary(worker_level)
    if salary != 0:
        print(f"The salary for worker level {worker_level} is ${salary}")
    else:
        print("Invalid worker level. Salary calculation failed.")


if __name__ == "__main__":
    main()

# Print grid(rows, columns)

def print_grid(rows, columns):
   
    for i in range(rows):
        print("+" + "---+" * columns)
        for _ in range(4):  # Each row is 4 units high
            print("|" + "   |" * columns)
    print("+" + "---+" * columns)


def main():
    print("Grid Printer")
    
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns should be positive integers")
    except ValueError as e:
        print("Invalid input. Please enter valid integers for rows and columns.")
        return

    print_grid(rows, columns)


if __name__ == "__main__":
    main()
