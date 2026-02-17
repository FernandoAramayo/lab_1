# 1.
def add_numbers():
    n = int(input("How many number do you want to add? "))
    nums = []
    for i in range(n):
        num = int(input(f"insert number {i+1}: "))
        nums.append(num)
    return nums


# 2.
def inverted_numbers(nums):
    print("Inverted numbers:")
    for num in nums:
        inv = str(num)[::-1]
        print(inv)


# 3.
def get_info():
    name = input("name: ")
    age = int(input("age: "))
    profession = input("profession: ")
    return [name, age, profession]


# 4.
def unique_values():
    x = int(input("How many numbers do you want to insert? "))
    nums = []
    for i in range(x):
        num = int(input(f"Insert number {i+1}: "))
        if num not in nums:
            nums.append(num)
    return nums


def main():
    nums = add_numbers()
    print(f"Total sum = {sum(nums)}\n")
    inverted_numbers(nums)
    info = get_info()
    print(
        f"Your name is {info[0]}, you are {info[1]} years old and you work as {info[2]}\n"
    )
    print(*unique_values())


main()
