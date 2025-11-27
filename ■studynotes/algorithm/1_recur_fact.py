'''
arr[0] = 1
arr[1] = 1
arr[n] = n * arr[n-1]
'''
#--------------------------------------------------

# 재귀함수
def recur1(n):
    if n <= 1:
        return 1
    else:
        return n * recur1(n-1)

#--------------------------------------------------

# 동적계획법
def recur2(n):
    arr = [0] * (n + 1)
    arr[0], arr[1] = 1, 1
    for i in range(2, n+1):
        arr[i] = i * arr[i - 1]
    return arr[n]

#--------------------------------------------------

# 메모이제이션
n = 5
arr = [0] * (n+1)
arr[0] = 1
arr[1] = 1
def recur3(n):
    if n >= 2 and arr[n] == 0: # 초기화상태면
        arr[n] = n * recur3(n-1)
    return arr[n]
