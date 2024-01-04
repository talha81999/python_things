""" Write a Python program to add 'ing' at the end
of a given string (length should be at least 3).
If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less
than 3, leave it unchanged.
"""


def add_ing_or_ly_at_the_end_of_string(message):
    if len(message) > 2:
        if message[-3:] == "ing":
            message += "ly"
        else:
            message += "ing"
    else:
        print("message should be above length 3")
    return message


message = input("Enter a message")
result = add_ing_or_ly_at_the_end_of_string(message)
print(result)
