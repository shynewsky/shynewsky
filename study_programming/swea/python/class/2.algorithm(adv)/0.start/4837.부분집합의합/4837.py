def create_subset():
    subset_list = []
    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        # 원소 N개를 갖고 있고, 원소의 합이 K일때
        if len(subset) == N and sum(subset) == K:
            subset_list.append(subset)
            
    return len(subset_list)

T = int(input()) # 테스트케이스
for test_case in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split()) # N 부분집합 원소 수, K 부분집합의 합
    print(f'#{test_case}',create_subset())

