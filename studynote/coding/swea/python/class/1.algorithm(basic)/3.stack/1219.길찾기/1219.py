# 인접 딕셔너리 생성함수
def prepare_dict():
    dictionary = {i:[] for i in range(V)}
    for i in range(E):
        n1, n2 = data[i*2], data[i*2+1]
        dictionary[n1].append(n2)
        # dictionary[n2].append(n1) # 단방향이므로 삭제
    return dictionary

# DFS 탐색 함수
def DFS_dict(start, get):
    s = [start]
    visited = [0] * V

    while s:
        current_node = s.pop()

        if current_node == get:
            return 1

        if visited[current_node] == 0: # 방문하지 않았으면
            visited[current_node] = 1 # 방문 처리

            for next_node in adj_dict[current_node]:
                if visited[next_node] == 0:
                    s.append(next_node)

    else:
        return 0

T = 10
for _ in range(1, T+1):

    test_case, N = map(int, input().split())
    data = list(map(int, input().split()))
    V, E = 100, len(data)//2

    adj_dict = prepare_dict()
    result = DFS_dict(0, 99)

    print(f'#{test_case}', result)


