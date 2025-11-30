from collections import deque

T = int(input()) # 테스트 케이수 수

for test_case in range(1, T+1):

    # 입력
    N, M = map(int, input().split()) # N개 숫자, 뒤로보내기 M번
    q = deque(map(int, input().split())) # N개 숫자

    q.rotate(-M)
    print(f'#{test_case}', q[0])
