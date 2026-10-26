# 펙토리얼(재귀)
def recur(n): # n * (n-1) * .. * 2 * 1
    if n == 0 or n == 1:
        return 1
    return n * recur(n-1)

def solution(n, r):
    a = recur(n)
    b = recur(n-r)
    c = recur(r)
    return int(a / (b * c))
