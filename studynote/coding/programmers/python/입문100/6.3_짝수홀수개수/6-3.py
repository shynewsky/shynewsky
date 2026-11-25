def solution(num_list):
    even = len([i for i in num_list if i % 2 == 0])
    odd = len([i for i in num_list if i % 2 == 1])
    return [even, odd]
