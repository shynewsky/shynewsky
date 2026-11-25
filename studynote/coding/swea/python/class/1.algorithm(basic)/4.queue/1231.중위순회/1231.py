# 수업코드 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def in_order(T): # 중위순회
    if T:
        in_order(left[T])
        print(tree[T], end= '')
        in_order(right[T])

# 수업코드 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

T = 10 # 테스트케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 정점 총 개수
    matrix = [list(input().split()) for _ in range(N)]

    # 비어있는 칸은 ''로 채우기
    for row in matrix:
        while len(row) != 4 :
            row += ['']

    # 정점번호 VLR
    # 루트번호 1

    # tree  : ['', 'W', 'F', 'F', 'O', 'T', 'A', 'E', 'S']
    # par   : [0, 0, 1, 1, 2, 2, 3, 3, 4]
    # left  : [0, 2, 4, 6, 8, 0, 0, 0, 0]
    # right : [0, 3, 5, 7, 0, 0, 0, 0, 0]

    tree = [''] * (N+1)
    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for row in matrix :

        # tree 리스트 만들기
        p = row[0] # 1
        alpha = row[1] # W
        tree[int(p)] = alpha

        if row[2] : # 2
            l = row[2]
            left[int(p)] = int(l)
            par[int(l)] = int(p)

        if row[3]:
            r = row[3]
            right[int(p)] = int(r)
            par[int(r)] = int(p)

    # print(tree)
    # print(par)
    # print(left)
    # print(right)

    # 관계도 만들기 끝 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    print(f'#{test_case} ', end='')
    in_order(1)

    if test_case != T:
        print()