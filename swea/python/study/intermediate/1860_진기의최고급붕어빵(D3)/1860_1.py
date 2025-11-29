import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    # N 사람, M 초마다, K 개, arr 도착하는 시간
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 풀이
    # 초마다 방문하는 사람들의 수를 배열로 만들어야 한다
    len_arr = len(arr)
    max_arr = max(arr)
    visitors = [0] * (max_arr + 1) # 카운팅 배열처럼
    for i in range(len_arr):
        visitors[arr[i]] += 1

    # M 초 지나면, 누적 붕어빵 += K 개
    # visitors 배열에서 1을 만날때마다 -= 1 개
    # visitors 배열에서 -1 이 생기면 Impossible, 아니면 Possible
    count = 0
    possible = True

    if visitors[0] > 0: # (주의) 0초에 손님이 왔을때
        possible = False
    else :
        for i in range(1, max_arr + 1): # 초 지남

            if i % M == 0 : # M 초마다 K 개씩 증가
                count += K

            if visitors[i] > 0 : # 손님이 왔을때
                if count > 0 : # 붕어빵이 있으면
                    count -= visitors[i] # (주의) 손님이 한번에 여러명 올때
                    visitors[i] = 0
                else : # 붕어빵이 없으면
                    possible = False
                    break
        else:
            possible = True


    if possible :
        print(f'#{test_case}', 'Possible')
    else :
        print(f'#{test_case}', 'Impossible')
