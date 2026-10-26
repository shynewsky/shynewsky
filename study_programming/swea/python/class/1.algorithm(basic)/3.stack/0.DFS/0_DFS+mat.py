import sys
sys.stdin = open('input.txt')

# 입력 받기
V, E = map(int, input().split())        # V 노드, E 간선
data = list(map(int, input().split()))  # 노드와 간선 관계도

# 인접행렬
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
for i in range(E) :
    n1, n2 = data[i*2], data[i*2+1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# 깊이우선탐색
def DFS_stack(start) :

    stack = [start] # 스택 배열 만들기
    visited = [0] * (V+1) # adj_matrtix 의 행/열 수와 같다

    while stack : # 스택이 빌때까지 돌린다
        current_node = stack.pop()

        if visited[current_node] == 0 : # 지금까지 pop() 한 적이 없는 것은 1로 변경
            visited[current_node] = 1
            print(current_node, end=' ')

            # visited[current_node][next_node] 가 아니라 adj_matrix[current_node][next_node]
            # visited[current_node] 가 아니라 visited[next_node]
            # stack.append(current_node) 가 아니라 stack.append(next_node)
            # next_node 가 3번 쓰인다

            for next_node in range(V, 0, -1) :
                if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0 :
                    stack.append(next_node)

DFS_stack(1)
