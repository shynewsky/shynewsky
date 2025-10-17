def solution(my_string, letter):
    new_string = ''
    for char in my_string :
        if letter != char :
            new_string += char
    return new_string
