"""
Write a Python program to remove
the nth index character from a nonempty string.
"""

def remove_char_at_given_index(message, index):
    message = message[0:index] + message[index + 1:]
    return message


text = input("Enter a text: ")
result = remove_char_at_given_index(text, 1)
print(result)
