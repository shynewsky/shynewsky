import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for _ in range(1, T+1):

    # 외계 숫자 : 지구 숫자
    num_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }

    # 입력
    test_case, count = input().split()
    arr = [num_dict[i] for i in input().split()]
    N = int(count)

    # 풀이
    arr.sort()
    reverse_dict = {v : k for k, v in num_dict.items()}
    arr = [reverse_dict[i] for i in arr]

    # 출력
    print(f'#{test_case}')
    print(' '.join(arr))
