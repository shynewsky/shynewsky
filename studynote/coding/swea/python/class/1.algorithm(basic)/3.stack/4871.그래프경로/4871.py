# 인접 딕셔너리 생성 함수
def prepare_dict(matrix):
    dictionary = {i : [] for i in range(V+1)} # 인접딕셔러니
    for n1, n2 in matrix:
        dictionary[n1].append(n2)
        # dictionary[n2].append(n1) # 단방향이므로 없어야한다
    return dictionary

# DFS 탐색 함수
def DFS_dict(start, get):

    if start == get:
        return 0

    s = [start]
    visited = [0] * (V+1)

    while s:
        current_node = s.pop()

        if current_node == get:
            return 1

        if visited[current_node] == 0: # 방문 안헀으면
            visited[current_node] = 1 # 방문 처리

            for next_node in adj_dict[current_node]:
                if visited[next_node] == 0: # 방문 안했으면
                    s.append(next_node)     # 스택에 추가

    else:
        return 0

T = int(input())
for test_case in range(1, T+1):

    V, E = map(int, input().split()) # 6 5
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split()) # 1 6

    adj_dict = prepare_dict(data) # 인접딕셔너리
    result = DFS_dict(S, G)

    print(f'#{test_case}', result)
