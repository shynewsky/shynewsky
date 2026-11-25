T = int(input())

for test_case in range(1, T+1) :

    N = int(input()) # 5 이상 50 이하

    # 행렬받는 방법
    # matrix = [list(map(int, input().split())) for _ in range(N)]
    # 행 받는 방법
    array = list(map(int, input().split()))

    #----------------------------------------------------------------------------

    # 1. array 에서 각 항목들의 발생횟수를 세고, 정수를 인덱스로 하는 counts 에 저장한다
    max_num = max(array)           # 최댓값을 구한다
    counts = [0] * (max_num + 1)   # 최댓값보다 1 큰 크기의 배열을 만든다
    for i in range(N) :            # array 순회
        counts[array[i]] += 1      # counts 배열 채우기

    # 2. 정렬된 집합에서 각 항목의 앞에 위치할 개수를 반영하기 위해 counts 의 원소를 조정한다
    # counts_before = [1, 3, 1, 1, 2]
    # counts_after = [1, 4, 5, 6, 8] 로 누적합 배열로 만든다
    for i in range(1, max_num + 1) :
        counts[i] += counts[i - 1]

    # 3. array 를 역순으로 순회하면서, counts 를 감소시키고, temp 에 삽입한다
    temps = [0] * N                 # array 랑 같은 크기의 배열 만들기
    for i in range(N-1, -1, -1) :   # array 를 역순으로 순회하면서
        counts[array[i]] -= 1               # count 에서 1을 감소시키고
        temps[counts[array[i]]] = array[i]  # temp 에 array 값을 넣는다

    #----------------------------------------------------------------------------

    print(f'#{test_case}', end='')
    for i in range(N) :
        print(f' {temps[i]}', end='')

    if test_case != T :
        print()
