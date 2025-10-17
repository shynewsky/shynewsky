T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력 받기
    # test : #1
    # length : 7041
    test, N = input().split()
    N = int(N)
    arr = list(input().split()) # 한 줄만 가져오는 방법

    # key : 외계 숫자체계
    # value : 지구 숫자체계
    num_dict = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

    # num_arr = []
    # for string in arr :
    #     num_arr += [num_dict[string]]
    num_arr = [num_dict[string] for string in arr]

    # 카운팅 정렬 사용

    counts = [0] * 10 # 0~9까지 숫자
    for i in range(N) :  # arr 순회
        counts[num_arr[i]] += 1

    for i in range(1, 10) : # counts 순회
        counts[i] += counts[i-1]

    temps = [0] * N  # arr 순회
    for i in range(N) : # arr 역순회
        counts[num_arr[i]] -= 1
        temps[counts[num_arr[i]]] = num_arr[i]

    # value 값으로 key 찾기
    new_arr = []
    for key, value in num_dict.items():
        for num in temps :
            if num == value :
                new_arr += [key]


    print(test)
    for string in new_arr :
        print(string, end=' ')
    print()



