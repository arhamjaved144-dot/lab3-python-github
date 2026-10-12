def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    return "odd
def calculate_percentage(obtained, total):
    if total == 0:
        return None
    return (obtained / total) * 100
def main():
    while True:
        print(" Calculator menu= ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        try:
            choice = int(input("Enter a number from 1 to 7: "))
        except ValueError:
            print("Please enter a whole number from 1 to 7.")
            continue

        if choice == 7:
            print("Leaving the calculator, Goodbye!")
            break

        elif choice in (1, 2, 3, 4):
            try:
                number_1 = float(input("Enter your first number: "))
                number_2 = float(input("Enter your second number: "))
            except ValueError:
                print("Kindly enter valid numbers.")
                continue

            if choice == 1:
                print("Addition:", add(number_1, number_2))
            elif choice == 2:
                print("Subtraction:", subtract(number_1, number_2))
            elif choice == 3:
                print("Multiplication:", multiply(number_1, number_2))
            else:
                result = divide(number_1, number_2)
                if result is None:
                    print("You cannot divide by zero.")
                else:
                    print("Division:", result)

        elif choice == 5:
            try:
                number = int(input("Enter a whole number: "))
            except ValueError:
                print("Please enter a valid whole number.")
                continue
            print("The number is", check_even_odd(number))

        elif choice == 6:
            try:
                obtained = float(input("Enter your obtained marks: "))
                total = float(input("Enter your total marks: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            result = calculate_percentage(obtained, total)
            if result is None:
                print("Total marks cannot be zero.")
            else:
                print("Percentage:", result, "%")

        else:
            print("Invalid choice. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
