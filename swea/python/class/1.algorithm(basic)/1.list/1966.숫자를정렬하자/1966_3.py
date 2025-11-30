T = int(input())

for test_case in range(1, T+1) :

    N = int(input()) # 5 이상 50 이하

    # 행렬받는 방법
    # matrix = [list(map(int, input().split())) for _ in range(N)]
    # 행 받는 방법
    array = list(map(int, input().split()))

    #----------------------------------------------------------------------------

    # 선택정렬
    # 범위(i)는 앞에서부터 줄어들고
    # '인덱스'로 '최솟값' 을 구하고
    # 두번째값(j)는 끝(N)까지 순회한다

    for i in range(N-1):

        min_idx = i                   # 가장 첫 인덱스를 최소값의 인덱스라고 설정하고
        for j in range(i+1, N):       # 범위의 두번째 인덱스부터 순회하며
            if array[min_idx] > array[j] :  # 최솟값인지 확인하고,
                min_idx = j           # 최소값을 구하는게 아니라, 최솟값의 인덱스를 구한다

        array[i], array[min_idx] = array[min_idx], array[i]  # 첫 값과, 찐 최소값 자리를 교환한다

    #----------------------------------------------------------------------------

    print(f'#{test_case}', end='')
    for i in range(N) :
        print(f' {array[i]}', end='')

    if test_case != T :
        print()
