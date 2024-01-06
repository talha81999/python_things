class ReplaceRepeatingCharWithDollar:
    def __init__(self):
        self.message = ""
        self.result = ""

    def replace_repeating_char_with_dollar(self, message):
        self.message = message
        for char in message:
            if char in self.result:
                self.result += "$"
            else:
                self.result += char


object1 = ReplaceRepeatingCharWithDollar()
object1.replace_repeating_char_with_dollar("message")
print(object1.result)
