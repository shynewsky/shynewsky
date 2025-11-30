import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1) :

    # arr = input() # 문자열은 불변형이라 arr[i], arr[N-1-i] = arr[N-1-i], arr[i] 이 불가능하다
    arr = list(input())
    N = len(arr)

    for i in range(N//2) :
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]

    print(''.join(arr))

