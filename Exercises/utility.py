# The built-in function 'max' can do the same thing this function can,
# so. Still a good exercise!
def find_highest(number_list):
    highest = number_list[0]
    for number in number_list:
        if number > highest:
            highest = number
    return highest
