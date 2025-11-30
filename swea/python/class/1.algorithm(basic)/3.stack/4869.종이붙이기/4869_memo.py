import sys
sys.stdin = open('input.txt')

# A(n) = A(n-1) + 2 * A(n-2)
def paper_memoization(n):
    if n >=2 and A[n] == 0:
        A[n] = paper_memoization(n-1) + 2 * paper_memoization(n-2)
    return A[n]

T = int(input())
for test_case in range(1,T+1):

    N = int(input())

    A = [0] * (N+1)
    A[0] = A[1] = 1
    result = paper_memoization(N//10)

    print(f'#{test_case}', result)

