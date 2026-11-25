# 입력
T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    total = 0                    # 이익
    count = 0                    # 주식 개수
    idx = 0                      # 오늘

    while idx < N:
        arr = data[idx:]                    # 남은 기한
        max_num = max(data[idx:])           # 매매가
        max_idx = arr.index(max_num) + idx  # 팔 날짜

        while True:
            # 판매
            if idx == max_idx:
                total += data[idx] * count
                count = 0
                idx += 1
                break
            # 구매
            total -= data[idx]
            count += 1
            idx += 1

    print(f'#{t}',total)


