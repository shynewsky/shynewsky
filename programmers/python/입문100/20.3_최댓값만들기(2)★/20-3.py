def solution(numbers):
    max_mul = numbers[0] * numbers[1]
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            mul = numbers[i] * numbers[j]
            if max_mul < mul:
                max_mul = mul

    return max_mul
