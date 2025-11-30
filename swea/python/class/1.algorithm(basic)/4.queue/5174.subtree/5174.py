from collections import deque

T = int(input()) # 테스트케이스 수 3

for test_case in range(1, T+1):

    # 입력
    E, N = map(int, input().split()) # E 간선개수, N 서브트리 루트
    arr = list(map(int, input().split())) # E쌍의 부모자식 번호쌍

    # 자식수 리스트 만들기
    # 노드는 1 ~ E+1 까지 존재
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # print('left', left)
    # print('right', right)

    # 자식찾기 - BFS
    q = deque([N])
    count = 1

    while q:
        root = q.popleft() # 큐에 들어간 자식노드를 활용하여 탐색한다
        if left[root] != 0: # 자식 노드를 큐에 넣는다
            q.append(left[root])
            count += 1
        if right[root] != 0: # 자식 노드를 큐에 넣는다
            q.append(right[root])
            count += 1
        # print('q', q)

    # print('root', root)
    # print('count', count)
    print(f'#{test_case}', count)
