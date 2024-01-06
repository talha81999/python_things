def factorial_fun(number):
    return 1 if number == 1 else number * factorial_fun(number - 1)


number = int(input("Enter a number to calculate factorial:  "))
result = factorial_fun(number)
print(f"The Factorial of {number} is {result}")
