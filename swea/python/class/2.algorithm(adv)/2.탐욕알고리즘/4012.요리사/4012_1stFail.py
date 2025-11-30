import sys
sys.stdin = open('input.txt')
from pprint import pprint

def recur(cnt, subsetA, subsetB):
    global subset_list

    # 가지치기 : 각 부분집합에 원소 두개씩만 허용
    if len(subsetA) > N//2:
        return
    if len(subsetB) > N//2:
        return

    # 깊이 : 식재료 수만큼
    if cnt == N:
        # AB = BA 조합이 같은 경우, 추가하지 않는다
        if sorted([subsetA[:], subsetB[:]]) not in subset_list:
            subset_list.append(sorted([subsetA[:], subsetB[:]]))
        return

    # A 부분집합 만들기
    subsetA.append(cnt + 1)
    recur(cnt+1, subsetA, subsetB)
    subsetA.pop()

    # B 부분집합 만들기
    subsetB.append(cnt + 1)
    recur(cnt+1, subsetA, subsetB)
    subsetB.pop()

def synergy():

    min_val = sum(matrix)
    for A, B in subset_list:
        val_A = val_B = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                val_A += A[i][j] + A[j][i]
                val_B += B[i][j] + B[j][i]
        val = val_A + val_B
        if min_val > val:
            min_val = val
    print(min_val)

    return min_val

T = int(input()) # 테스트케이스
for t in range(1, T+1):
    # 입력
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 풀이
    # 1) 부분집합 조합 구하기
    subset_list = []
    recur(0, [], [])
    # 2) 시너지 최소값 구하기
    answer = synergy()
    # 출력
    print(f'#{t}',)

