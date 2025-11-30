import sys
sys.stdin = open('input.txt')

# A(n) = A(n-1) + 2 * A(n-2)
def paper_dp(n):
    A = [0] * (n+1)
    A[0] = A[1] = 1
    for i in range(2, n+1):
        A[i] = A[i-1] + 2 * A[i-2]
    return A[n]

T = int(input())
for test_case in range(1,T+1):

    N = int(input())
    result = paper_dp(N//10)

    print(f'#{test_case}', result)
