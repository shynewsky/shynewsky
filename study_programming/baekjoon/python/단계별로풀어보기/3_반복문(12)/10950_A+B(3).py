T = int(input()) # 테스트 케이스 수
arr = [list(map(int, input().split())) for _ in range(T)]

for A, B in arr:
    print(A + B)
