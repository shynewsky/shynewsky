# 1. 노가다

def solution(hp):
    a = hp // 5
    hp -= a * 5
    b = hp // 3
    hp -= b * 3
    c = hp // 1
    return a + b + c

# 2. divmod()

def solution(hp):
    num = [5, 3, 1]
    ans = []
    for i in num :
        div, mod = divmod(hp, i)
        ans.append(div)
        hp = mod
    return sum(ans)
