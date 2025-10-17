#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    
    N, M = map(int, input().split())  # N 정수의 개수, M 구간의 개수
    data = list(map(int, input().split()))  # arr N개의 정수 리스트

    sum_list = []
    for i in range(0, N-M+1) :
        sum_num = 0
        for j in range(i, i+M) :
            sum_num += data[j]
        sum_list += [sum_num]

    min_sum = sum_list[0]
    max_sum = sum_list[0]
    for i in range(0, len(sum_list)) :
        if min_sum > sum_list[i] :
            min_sum = sum_list[i]            
        if max_sum < sum_list[i] :
            max_sum = sum_list[i]

    print(f'#{test_case} {max_sum - min_sum}')