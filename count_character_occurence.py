
# my code

# message = "google.com"
# newList = []
# ne = []
#
# for i in range(len(message)):
#     count = 0
#     for j in range(len(message)):
#         if message[i] == message[j]:
#             count += 1
#     if message[i] not in ne:
#         newList.insert(i, message[i] + ": " + str(count))
#         ne.insert(0, message[i])
#
# print(newList)


# chatgpt code

message = "google.com"
char_count = {}
for char in message:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)
