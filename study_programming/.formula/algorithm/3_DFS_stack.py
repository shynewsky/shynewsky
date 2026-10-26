# DFS(스택)
'''
start는 입력받는다
stack 리스트를 start로 초기화한다
visited 를 패딩하여 만든다

"스택이 빌때까지 반복하여 돈다"
    현재 원소를 지정한다

    방문하지 않은경우,
        방문처리하고
        출력하고

        현재 행의 오른끝에서부터 내려오면서 다음 원소를 지정한다
            만약 간선이 있고, 방문한 적이 없으면
                다음 방문지점으로 스택에 추가한다
'''

#--------------------------------------------------

# 인접행렬

def DFS1(start): 
    s = [start]
    visited = [0] * (V+1)
    result = []

    while s:
        current_node = s.pop()

        if visited[current_node] == 0:
            visited[current_node] = 1
            result.append(current_node)

            for next_node in range(V, 0, -1): # 큰수부터
                if adj_mat[current_node][next_node] == 1 and visited[next_node] == 0:
                    s.append(next_node)

    return result

#--------------------------------------------------











# 인접리스트

def DFS2(start): 
    for i in range(1, V+1): # 큰수부터
        adj_list[i].sort(reverse=True)

    s = [start]
    visited = [0] * (V+1)
    result = []

    while s:
        current_node = s.pop()

        if visited[current_node] == 0:
            visited[current_node] = 1
            result.append(current_node)

            for next_node in adj_list[current_node]:
                if visited[next_node] == 0:
                    s.append(next_node)

    return result

#--------------------------------------------------

# 인접딕셔너리

def DFS3(start): 
    s = [start]
    visited = [0] * (V+1)
    result = []

    while s:
        current_node = s.pop()

        if visited[current_node] == 0:
            visited[current_node] = 1
            result.append(current_node)

            for next_node in sorted(adj_dict[current_node], reverse=True):# 큰수부터
                if visited[next_node] == 0:
                    s.append(next_node)

    return result
