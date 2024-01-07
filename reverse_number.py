number = int(input("Enter number: "))
reverse_number = 0
while number > 0:
    dig = number % 10
    reverse_number = reverse_number * 10 + dig
    number = number // 10
print("Reverse of the number:", reverse_number)
