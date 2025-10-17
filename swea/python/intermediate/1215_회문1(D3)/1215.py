T = 10 # 테스트 케이스

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 찾아야하는 회물 길이
    matrix = [input() for _ in range(8)]

    # 풀이
    total_count = 0

    for row in matrix : # 행에서
        for j in range(8 -(N-1)): # 열이 이동할 수 있는 범위
            if row[j:j+N] == row[j:j+N][::-1]: # 순서대로 읽었을때, 거꾸로 읽은것과 같다면
                total_count += 1

    for col in zip(*matrix): # 열에서 (전치행렬로 바꾼후 행에서)
        for i in range(8 - (N-1)): # 행이 이동할 수 있는 범위
            if col[i:i+N] == col[i:i+N][::-1]: # 순서대로 읽었을때, 거꾸로 읽은것과 같다면
                total_count += 1

    print(f'#{test_case}', total_count)