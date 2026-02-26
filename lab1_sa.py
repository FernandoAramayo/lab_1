# 1. Adds n numbers
def add_n_numbers():
    n = int(input("How many numbers do you want to add? "))
    total = 0
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        total += num
    print("Sum =", total)


# 2. Inverts a number (e.g., 619 -> 916)
def invert_number():
    number = input("Enter a number to invert: ")
    inverted = number[::-1]
    print("Inverted number =", inverted)


# 3. Asks name, age, profession and prints custom message
def user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    profession = input("Enter your profession: ")
    print(f"\nHello {name}! You are {age} years old and work as a {profession}. Keep growing professionally!")


# 4. Asks x numbers and returns only unique values
def unique_values():
    x = int(input("How many numbers will you enter? "))
    values = []
    for i in range(x):
        num = input(f"Enter value {i+1}: ")
        values.append(num)

    unique = list(set(values))
    print("Unique values:", unique)


def main():
    while True:
        print("\n--- MENU ---")
        print("1. Add n numbers")
        print("2. Invert a number")
        print("3. User information")
        print("4. Unique values")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_n_numbers()
        elif choice == "2":
            invert_number()
        elif choice == "3":
            user_info()
        elif choice == "4":
            unique_values()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
