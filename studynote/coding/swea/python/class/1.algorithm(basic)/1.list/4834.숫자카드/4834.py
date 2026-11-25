#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    # 카운팅 정렬의 '숫자는 인덱스로, 횟수는 원소로' 나타내는 개념을 사용할 것이다
    # 0~9 까지의 숫자만 나올것이기 때문에, 원소 10개를 갖는 배열을 먼저 선언한다
    # 입력값이 문자열이기 때문에, 문자열을 for 문으로 순회하며, 한 문자씩 떼어낼 것이고
    # 떼어낸 문자를 숫자로 바꾼뒤에, 그 숫자에 해당하는 인덱스를 찾아, 원소 개수를 += 1 해줄 것이다

    count_list = [0] * 10  # 원소 10개를 갖는 배열을 선언한다
    
    #for char in input() :    # 문자열 분해
    for char in str(int(input())) :    # 문자열 분해 ㅡ \n 을 숫자로 변환할때 문제가 생김
        count_list[int(char)] += 1    # 인덱스가 숫자인 위치에 += 1 을 한다

    # 횟수가 적힌 리스트에서 가장 높은 횟수를 찾고, (만약 횟수가 같다면 높은 숫자를 뽑고 - 최댓값 마지막 인덱스)
    # 해당 인덱스를 반환한다

    max_num = count_list[0]
    max_count = 0
    index_num = -1

    for num in count_list :
        index_num += 1
        if max_num <= num :
            max_num = num
            max_count = index_num

    print(f'#{test_case} {max_count} {max_num}')
