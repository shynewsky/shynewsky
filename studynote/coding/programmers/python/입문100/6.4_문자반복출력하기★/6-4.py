def solution(my_string, n):
    new_string = ''
    for char in my_string :
        new_string += (char * n)
    return new_string
