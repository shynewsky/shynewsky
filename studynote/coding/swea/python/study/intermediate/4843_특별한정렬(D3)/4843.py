T = int(input()) # 테스트케이스

for test_case in range(1, T+1) :

    # 입력 받기
    N = int(input()) # 정수의 개수 (10 <= N <= 100)
    arr = list(map(int, input().split())) # N개의 정수 (1 <= arr[i] <= 100)

    # 선택정렬을 사용한다
    # for _ in range(0, len(arr)) 에서 ㅡ 짝수번째에는 max, 홀수번째에는 min 을 구한다
    for i in range(0, N) :

        if i % 2 == 0 : # 짝수번째에는 max 구하기

            max_idx = i # 최댓값 구하기 ㅡ 원소가 아닌 인덱스로 활용해야, 교환할때 적용된다
            for j in range(i, N) :
                if arr[max_idx] < arr[j] :
                    max_idx = j # 원소가 아닌 인덱스로 활용해야, 자리 교환할때 적용된다

            arr[i], arr[max_idx] = arr[max_idx], arr[i]  # 구간 내 첫번째 원소랑 자리 교환

        else : # 홀수번째에는 min 구하기

            min_idx = i # 최솟값 구하기 ㅡ 원소가 아닌 인덱스로 활용해야, 교환할때 적용된다
            for j in range(i, N) :
                if arr[min_idx] > arr[j] :
                    min_idx = j # 원소가 아닌 인덱스로 활용해야, 자리 교환할때 적용된다

            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 구간 내 첫번째 원소랑 자리 교환

    # 출력 하기
    print(f'#{test_case}', end='')
    for i in range(10):
        print(f' {arr[i]}', end='')

    if test_case != T :
        print()