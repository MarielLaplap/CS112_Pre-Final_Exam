print("""
CS112: Computer Programming 1 - PRE-FINAL EXAM
Created by: Mariel Laplap

Problem: Create a python program that displays all prime numbers within a range:

RULES TO CONSIDER:
[1] If number[start] is a negative number, prompt: "Enter a non-negative number"
[2] If number[end] is less than number[start], prompt: "Enter a number greater than number[start]"
[3] If the user enters the number "0", terminate the program.
""")


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


while True:  # Main Program
    start = int(input("Enter a number [start]: "))

    if start < 0:
        print("Enter a non-negative number.")
        print()
        continue

    if start == 0:
        print("Program terminated.")
        break

    end = int(input("Enter a number [end]: "))

    if end <= start:
        print("Enter a number greater than", start)
        print()
        continue

    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

    print("\n")
