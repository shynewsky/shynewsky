def solution(numbers):
    dictionary = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    N = len(numbers)

    i = c = 0
    stack = []

    while i < N:
        for key, value in dictionary.items():
            if numbers[i:i+c] == key:
                stack.append(str(value))
                i += c
                c = 0
        c += 1

    return int(''.join(stack))
