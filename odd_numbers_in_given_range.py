def odd_numbers_in_range(num):
    odd_num_list = []
    for i in range(num + 1):
        if i % 2 == 1:
            odd_num_list.append(i)
    return odd_num_list


number = int(input("Enter a number:  "))
result = odd_numbers_in_range(number)
print(result)
