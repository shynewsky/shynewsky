T = int(input())
for t in range(1, T+1):
    N = int(input()) # 거스름돈

    q_cnt = N // 25
    N %= 25
    d_cnt = N // 10
    N %= 10
    n_cnt = N // 5
    N %= 5
    p_cnt = N // 1

    print(q_cnt, d_cnt, n_cnt, p_cnt)
