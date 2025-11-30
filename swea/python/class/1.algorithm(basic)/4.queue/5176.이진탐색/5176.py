T = int(input()) # 테스트케이스

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 1~N 까지 노드

    # 풀이
    # 비어있는 완전이진트리 만들어놓고
    # 중위순회를 하며 값을 1부터 N까지 채우자

    arr = [i for i in range(1, N+1)] # 넣을 원소들
    tree = [0] * (N+1) # 원소가 들어갈 자리

    stack = [] # 깊게 내려가는 동안 지나가는 노드 쌓을 곳
    arr_idx = 0 # 가장 깊은곳에서, [0]번부터 넣을 것이다
    tree_idx = 1 # 현재 위치한 위치 번호 ㅡ N/2를 버림하여 출력해야한다

    while True:

        # 왼쪽 가장 깊은 곳까지 1~N까지 [위치 번호] 채우면서 내려가기
        while tree_idx <= N:
            stack.append(tree_idx)
            tree_idx *= 2   # 왼쪽으로 내려갈때는 짝수번으로 내려가야한다

        if not stack: # 스택에 값이 있는 동안만 순회
            break

        # 왼쪽 가장 깊은 곳까지 내려갔을때, 위치번호를 [배열 원소]로 바꾸면서 올라가기
        tree_idx = stack.pop() # 올라가면서 가장 가까운 부모 원소에서 다시 형제 찾기
        tree[tree_idx] = arr[arr_idx] # [위치 번호]룰 [배열 원소]로 바꾸기
        arr_idx += 1 # 다음 배열 원소로 지정

        # 왼쪽 넣었으면, 이제 부모노드의 오른쪽으로 이동
        tree_idx = tree_idx * 2 + 1

    # 트리 만들기 끝 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    # tree[1] : 루트노드
    # tree[N//2] : 찾는노드

    print(f'#{test_case}', tree[1], tree[N//2])