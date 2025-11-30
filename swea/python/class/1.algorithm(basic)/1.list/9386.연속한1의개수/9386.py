#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    str_arr = input().split('0')
    
    max_count = 0

    for i in range(len(str_arr)) :

        if not str_arr[i] :
            continue

        count = 0
        for i in str_arr[i] :
            count += 1

        if max_count < count :
            max_count = count

    print(f'#{test_case} {max_count}')
