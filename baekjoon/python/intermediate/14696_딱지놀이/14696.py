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

    # 길이가 긴걸 B로 한다
    lenA, lenB = len(A), len(B)
    if lenA > lenB:
        a, A, lenA, b, B, lenB = b, B, lenB, a, A, lenA

    # print(a, A, lenA)
    # print(b, B, lenB)

    # 긴 배열 위주로 순회
    winner = 'D'
    for i in range(lenB):

        if i > lenA-1: # 작은 배열 끝났으면
            winner = 'B'
            break

        if A[i] == B[i]: # 같으면 다음으로 넘기기
            continue
        elif A[i] > B[i]:
            winner = 'A'
            break
        elif A[i] < B[i]:
            winner = 'B'
            break

    print(winner)


