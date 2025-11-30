def recur(i, cnt):
    global min_cnt

    if i > N-1: # 종료조건
        cnt -= 1
        if min_cnt > cnt:
            min_cnt = cnt
        return

    if cnt > min_cnt: # 가지치기
        return

    for j in range(1, arr[i]+1):
        recur(i+j, cnt+1)

T = int(input())
for t in range(1, T+1):
    # 입력
    arr = list(map(int, input().split()))
    # 전처리
    N = arr[0]
    arr[0] = 0
    min_cnt = sum(arr)
    # 풀이
    recur(1, 0) # i=1, cnt=0 부터 시작
    # 출력
    print(f'#{t}', min_cnt)