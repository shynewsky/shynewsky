T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N, K = map(int, input().split()) # N개 과목, K개 선택
    scores = sorted(map(int, input().split())) # 성적을 오름차순으로 가져온다

    max_sum = sum(scores[N-1:N-1-K:-1])
    print(f'#{test_case}', max_sum)