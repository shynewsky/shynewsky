import sys
sys.stdin = open('input.txt')

# 입력 -----------------------

N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))

# 코드 ------------------------

# N장의 카드 (3 ≤ N ≤ 100)
# 3장의 카드 선택
# M을 넘지 않게 카드의 합을 최대한 크게 (10 ≤ M ≤ 300,000)

max_val = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            val = li[i]+li[j]+li[k]
            if M < val:
                break
            if max_val < val:
                max_val = val

print(max_val)

