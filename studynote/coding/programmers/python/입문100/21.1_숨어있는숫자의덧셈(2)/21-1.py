def solution(my_string):
    string = ''
    for s in my_string:
        try:
            string += str(int(s))
        except:
            string += ' '
    str_list = string.split(' ')
    num_list = []
    for i in str_list:
        if i != '':
            num_list += [int(i)]
    return sum(num_list)
