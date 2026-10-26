# 수식이진트리 계산 ----------------------------------------
def func(p):
    val = token[p]

    # 피연산자일때
    if val.isdigit() : return float(val)

    # 연산자일때
    a = func(left[p])
    b = func(right[p])
    if val == '+' : return a+b
    elif val == '-' : return a-b
    elif val == '*' : return a*b
    elif val == '/' : return a/b

# 입력 ---------------------------------------------------
T = 10
for t in range(1, T+1):
    V = int(input()) # 정점개수

    # 수식이진트리 생성 -------------------------------------

    token = [""] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)

    for _ in range(V):
        temp = input().split()
        idx = int(temp[0])
        if len(temp) == 2:
            token[idx] = temp[1]
        else:
            token[idx] = temp[1]
            left[idx] = int(temp[2])
            right[idx] = int(temp[3])

# 설계 ----------------------------------------------------

    "수식이진트리"
    # - 부모는 연산자, 자식은 피연산자
    # - 포화(X), 완전(X)
    # - 후위순회 : 피연산자

    # 입력방식
    # 1) 정점번호, 연산자, 자식정점번호, 자식정점번호
    # 2) 정점번호, 양의 정수
    # - 루트정점은 항상 1
    '''
    부모정점번호 : 부모정점원소 : 자식정점번호
    1 : - : {2, 3}
    2 : - : {4, 5}
    3 : 10 : {}
    4 : 88 : {}
    5 : 65 : {}
    '''
    '''
    token = ["", "-",  "-",  "10", "88", "65"]
    left  = [0,  2,    4,    0,    0,    0]
    right = [0,  3,    5,    0,    0,    0]
    '''

    # 구해야할것 : 수식의 결과값

# 코드 ----------------------------------------------------

    print(f'#{t}', int(func(1)))




