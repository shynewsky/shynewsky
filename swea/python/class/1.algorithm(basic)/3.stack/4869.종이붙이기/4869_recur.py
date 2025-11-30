import sys
sys.stdin = open('input.txt')

# A(n) = A(n-1) + 2 * A(n-2)
def paper_recursive(n):
    if n == 0 or n == 1: # 종료 조건
        return 1
    return paper_recursive(n-1) + 2 * paper_recursive(n-2)


T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    result = paper_recursive(N//10)

    print(f'#{test_case}', result)
