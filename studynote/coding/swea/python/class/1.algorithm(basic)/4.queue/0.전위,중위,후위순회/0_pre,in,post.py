'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(T): # 전위순회
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])

def in_order(T): # 중위순회
    if T:
        in_order(left[T])
        print(T)
        in_order(right[T])

def post_order(T): # 후위순회
    if T:
        post_order(left[T])
        post_order(left[T])
        print(T)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 입력
N = int(input())
E = N-1
arr = list(map(int, input().split()))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 올라가는 용도 (자식에서 부모 찾기)
par = [0] * (N+1)

# 내려가는 용도 (부모에서 자식찾기)
left = [0] * (N+1) # 왼쪽 자식 저장
right = [0] * (N+1) # 오른쪽 자식 저장

# 부모-자식 노드 연결
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    # 올라가는 용도
    par[c] = p

    # 내려가는 용도
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 루트 노드 찾기
root = 1
for i in range(1, N+1):
    if par[i] == 0 : # 부모가 없으면
        root = i
        break

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 루트 노드부터 순회하기
pre_order(root)  # 전위 순회
in_order(root)   # 중위 순회
post_order(root) # 후위 순회

