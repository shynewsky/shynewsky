X = int(input())  # 총 금액
N = int(input())  # 물건 종류 수
arr = [list(map(int, input().split())) for _ in range(N)]  # 영수증

total_cost = 0
for a, b in arr:
    total_cost += a * b

if total_cost == X:
    print('Yes')
else:
    print('No')
