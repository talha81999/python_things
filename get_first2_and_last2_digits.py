# my code
class StringPractice:
    result = ""

    @staticmethod
    def getFirstTwoAndLastTwoDigitsInString(message):
        if len(message) < 2:
            StringPractice.result = "Empty string"
        else:
            StringPractice.result = message[0] + message[1] + message[len(message) - 2] + message[len(message) - 1]
        return StringPractice.result

object1 = StringPractice()
object1.getFirstTwoAndLastTwoDigitsInString("google")
print(object1.result)

# chatgpt code
class StringPractice:
    @staticmethod
    def getFirstTwoAndLastTwoDigitsInString(message):
        if len(message) < 2:
            return "Empty string"
        return message[:2] + message[-2:]


# Example usage
result = StringPractice.getFirstTwoAndLastTwoDigitsInString("google")
print(result)

