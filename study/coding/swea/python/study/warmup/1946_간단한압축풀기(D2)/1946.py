# 입력
T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]

    total = ''
    count = 0
    for a, b in data:
        total += a * int(b)
        count += int(b)

    idx = 0
    print(f'#{t}')
    while idx < count:
        print(total[idx:idx+10])
        idx += 10