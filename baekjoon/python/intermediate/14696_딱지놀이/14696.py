import sys
sys.stdin = open('input.txt')

# 입력 ----------------------------------------

N = int(input()) # 라운드 수 (1<=N<=1000)
for _ in range(N): # A,B 돌아가면서 N 라운드
    a, *A = list(map(int, input().split()))
    A.sort(reverse=True)
    b, *B = list(map(int, input().split()))
    B.sort(reverse=True)

    # 코드 -------------------------------------

    lenA, lenB = len(A), len(B)

    # 길이가 긴걸 B로 한다 ㅡ 답이 달라진다
    # if lenA > lenB:
    #     a, A, lenA, b, B, lenB = b, B, lenB, a, A, lenA

    min_len = lenA if lenA < lenB else lenB

    # 긴 배열 위주로 순회
    winner = 'D'
    for i in range(min_len):
        if A[i] == B[i]:
            continue
        elif A[i] > B[i]:
            winner = 'A'
            break
        elif A[i] < B[i]:
            winner = 'B'
            break
    else:
        winner = 'A' if lenA > lenB else 'B' if lenB > lenA else 'D'

    print(winner)
