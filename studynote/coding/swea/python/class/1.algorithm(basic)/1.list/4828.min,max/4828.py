#import sys
#sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]

    for i in range(0, N):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]

    print(f'#{test_case} {max_num - min_num}')