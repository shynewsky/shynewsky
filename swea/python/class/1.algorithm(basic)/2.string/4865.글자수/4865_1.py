import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    # 입력 받기
    str1 = list(set(input())) # set() 으로 받아서 중복 제거 ㅡ 개수, 순서 상관 없으므로 괜찮을 듯
    str2 = list(input())

    # 최대개수 구하기

    max_count = 0

    for char1 in str1 : # 찾으려는 문자를 순회

        count = 0

        for char2 in str2 : # 전체 문자를 순회
            if char1 == char2 :
                count += 1

        if max_count < count :
            max_count = count

    print(f'#{test_case} {max_count}')

