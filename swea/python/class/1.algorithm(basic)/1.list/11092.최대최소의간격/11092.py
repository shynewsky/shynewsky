#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))
    
    max_num = arr[0]
    min_num = arr[0]
    max_idx = 0
    min_idx = 0
    
    for i in range(N) :
        if max_num <= arr[i] :
            max_num = arr[i]
            max_idx = i
        if min_num > arr[i] :
            min_num = arr[i]
            min_idx = i
            
    print(f'#{test_case} {abs(max_idx - min_idx)}')