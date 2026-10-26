def solution(numbers, k):
    for i in range(k-1):
        n1 = numbers.pop(0)
        n2 = numbers.pop(0)
        numbers.append(n1)
        numbers.append(n2)
    return numbers[0]
