T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N, K = map(int, input().split()) # 전체 N명, 제출한사람 K명
    arr = sorted(list(map(int, input().split()))) # 제출한사람 번호를 나열하여 가져온다

    # 풀이
    temp = [str(i) for i in range(1, N+1) if i not in arr]

    # 출력
    print(f'#{test_case}', ' '.join(temp))