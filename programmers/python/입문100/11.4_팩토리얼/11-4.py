def solution(n):
    i = 1
    ans = i
    while ans * i < n:
        i += 1
        ans *= i
    return i
