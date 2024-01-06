"""
Write a Python function that takes a list of words
and return the longest word and the length
of the longest one.
"""


def find_longest_word_in_given_string(text):
    list_of_words = text.split(" ")
    length_of_word = 0
    text_of_word = ""
    for word in list_of_words:
        if len(word) > length_of_word:
            length_of_word = len(word)
            text_of_word = word
    return [length_of_word, text_of_word]


message = input("Enter a message: ")
result = find_longest_word_in_given_string(message)
print(result)
