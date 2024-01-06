def get_table_of_a_given_number(num, temp ):
    if temp <= 10:
        result = num * temp
        print(f"{number} * {temp} = {result}")
        temp += 1
        get_table_of_a_given_number(num, temp)
    else:
        return 0


number = int(input("Enter a number:  "))
temp_num = 1
get_table_of_a_given_number(number, temp_num)
