import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 정수 개수
    arr = list(map(int, input().split())) # [2, 4, 7, 10]

    # 풀이
    max_mul = -1 # 갱신되지 않으면 -1로 바로 나올 수 있도록

    for i in range(N-1): # 기준점 이동
        for j in range(i+1, N): # 비교점 이동
            num = arr[i] * arr[j] # Ai * Aj 구해서
            string = str(num)     # 문자열로 변환 후
            isIncrease = True     # 증가하는지 호가인

            for k in range(len(string)-1): # string 을 순회하며
                if string[k] > string[k+1]: # 버블정렬처럼 이웃한 문자끼리 비교
                    isIncrease = False     # 뒤에 작은 수가 오면 False
                    break

            if isIncrease and max_mul < num :
                max_mul = num

    print(f'#{test_case} {max_mul}')
