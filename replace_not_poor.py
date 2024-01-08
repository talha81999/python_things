"""
Write a Python program to find the first appearance
of the substrings 'not' and 'poor' in a given string.
If 'not' follows 'poor', replace the
whole 'not'...'poor' substring
with 'good'. Return the resulting string.
"""


def replace_not_poor(text):
    findNot = text.find("not")
    findPoor = text.find("poor")
    if findNot != -1 and findPoor != -1:
        newText = text[findNot: findPoor + 4]
        if findPoor > findNot:
            text = text.replace(newText, "good")
    else:
        pass
    return text


message = input("Enter a message")
result = replace_not_poor(message)
print(result)
