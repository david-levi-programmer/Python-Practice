def find_highest(number_list):
    highest = number_list[0]
    for number in number_list:
        if number > highest:
            highest = number
    return highest
