import math

def task1():
    n = int(input("Please enter a positive integer greater than 9: "))
    steps = 0
    sequence = [str(n)]

    while n > 9:
        sum_digits = 0
        temp = n
        while temp > 0:
            sum_digits += temp % 10
            temp //= 10

        n = sum_digits
        sequence.append(str(n))
        steps += 1

    print(" \u2192 ".join(sequence))
    print(f"Final value: {n}")
    print(f"Total steps: {steps}\n")

def task2():
    prompt = "Please enter a number between 10 and 100: "

    while True:
        n = int(input(prompt))
        if 10 <= n <= 100:
            break
        prompt = "Invalid input. Please enter a number between 10 and 100: "

    fizz = 0
    buzz = 0
    fizzbuzz = 0

    for i in range(1, n + 1):
        if i % 7 == 0:
            print(f"({i} is skipped)")
            continue
        if i % 15 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(i)

    print("Summary")
    print(f"Fizz count: {fizz}")
    print(f"Buzz count: {buzz}")
    print(f"FizzBuzz count: {fizzbuzz}\n")

def task3():
    n = int(input("Please enter a number between 3 and 9: "))

    for i in range(1, 2 * n):
        k = n - abs(n - i)
        for j in range(1, k + 1):
            print(j, end="")
        print()

if __name__ == "__main__":
    print("--- Task 1 ---")
    task1()
    print("--- Task 2 ---")
    task2()
    print("--- Task 3 ---")
    task3()