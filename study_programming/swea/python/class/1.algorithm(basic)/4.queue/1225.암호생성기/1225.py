from collections import deque

T = 10 # 테스트 케이수 수

for _ in range(1, T+1):

    # 입력
    test_case = int(input()) # 테스트 케이스 번호
    q = deque(map(int, input().split())) # 숫자 8개
    s = deque([1, 2, 3, 4, 5]) # 5까지 증가하고 끝나면 다시 1빼기로 돌아온다

    # 풀이
    while True :

        num = q.popleft()
        sub = s.popleft()
        num -= sub
        s.append(sub)

        if num > 0 :
            q.append(num)
        else :
            q.append(0)
            break

    # 출력
    print(f'#{test_case}', *q)