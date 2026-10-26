# 평탄화
# 최고점 = > 최저점 1 개씩 옮기기
# 일차원 배열에서 최대 최소 찾기 문제
# 1. 그냥 최대 최소를 매번 찾아서 덤프 횟수 만큼 덤프
# 2. 카운팅 배열을 만들어서 최대 최소 찾기.
# ex) 14, 13, 11, 2, 3, 4, 5, 8, 11, 14
# 카운팅 배열을 만드는 순간 정렬이 된다.

T = 10  # 테스트 케이스의 수

for tc in range(1, T + 1):

    N = int(input())  # 덤프 횟수
    heights = list(map(int, input().split()))  # 상자의 높이

    for _ in range(N):  # 덤프 횟수만큼 반복 돌기
        # heights에서 최대, 최소
        # 최대 -1, 최소 +1

        # 최대값 찾기
        # - 임시 변수 max_val : 최소값(문제에서 주어지는 범위보다 작은값)으로 초기화
        #   상자의 높이 범위는 1이상 100이하.
        # - 반복을 돌면서 리스트의 각 원소와 임시변수 max_val 1:1 비교
        #   만약, 리스트의 원소가 max_val보다 크다면, max_val을 해당 원소로 업데이트.

        ## 나중에 heights 리스트에서 최대값을 -1 해야 하므로, 최대값의 인덱스를 기억해두어야함
        # => 최대값을 찾으면서 인덱스도 같이 저장!

        max_val = 0  # 최대값을 구할 때는 최소값으로 초기화
        max_idx = -1  # 인덱스는 -1로 초기화
        min_val = 101  # 최소값을 구할 때는 최대값으로 초기화
        min_idx = -1

        for idx in range(len(heights)):  # heights 길이 만큼 반복
            if heights[idx] > max_val:
                max_val = heights[idx]
                max_idx = idx  # 최대값을 찾으면서 해당 최대값의 idx도 같이 기억
            if heights[idx] < min_val:
                min_val = heights[idx]
                min_idx = idx

        heights[max_idx] -= 1
        heights[min_idx] += 1

        # if max_val - min_val <= 1:
        #     break

        # 평탄화 작업 끝(덤프 끝).
        # 마지막 덤프 수행하면서, 최대값과 최소값이 바뀜.
        # 최대 높이와 최소 높이 차를 구하기 위해서 최대 최소를 한 번 더 찾아야 함.

        max_val = 0  # 최대값을 구할 때는 최소값으로 초기화
        max_idx = -1  # 인덱스는 -1로 초기화
        min_val = 101  # 최소값을 구할 때는 최대값으로 초기화
        min_idx = -1

    for idx in range(len(heights)):  # heights 길이 만큼 반복
        if heights[idx] > max_val:
            max_val = heights[idx]
            max_idx = idx  # 최대값을 찾으면서 해당 최대값의 idx도 같이 기억
        if heights[idx] < min_val:
            min_val = heights[idx]
            min_idx = idx

    print(f"#{tc} {max_val - min_val}")
