def palindrome_number(num):
    store_number = ""
    for i in range(len(num) - 1, -1, -1):
        store_number += num[i]
    return "Palindrome number" if num == store_number else "not a palindrome number"


number = input("Enter a number:  ")
result = palindrome_number(number)
print(f"{number} is {result} ")
