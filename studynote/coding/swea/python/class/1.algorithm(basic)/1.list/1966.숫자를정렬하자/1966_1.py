T = int(input())

for test_case in range(1, T+1) :

    N = int(input()) # 5 이상 50 이하

    # 행렬받는 방법
    # matrix = [list(map(int, input().split())) for _ in range(N)]
    # 행 받는 방법
    array = list(map(int, input().split()))

    #----------------------------------------------------------------------------

    # 버블정렬
    # 범위(i)는 뒤에서부터 줄어들고
    # 기준값(j)는 앞에서부터 이동한다

    for i in range(N-1, 0, -1) : # i 로 범위를 뒤에서부터 좁혀온다
        for j in range(0, i) :   # i 는 뒷쪽 범위를 뜻한다
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

    print(f'#{test_case}', end='')
    for i in range(N) :
        print(f' {array[i]}', end='')

    if test_case != T :
        print()
