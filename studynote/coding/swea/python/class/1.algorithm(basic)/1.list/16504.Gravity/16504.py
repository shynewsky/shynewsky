#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    box_list = list(map(int, input().split()))
    
    # 기준이 되는 원소의 오른쪽으로, 해당 원소보다 작은 원소의 개수가 낙차이다
    # 기준 원소보다 오른쪽에 있는 작은 원소의 개수를 count_list 에 모은다
    
    count_list = []
    for i in range(N) : # len(box_list) 대신 N 을 사용한다 ㅡ len() 사용 자제
        count = 0
        base_box = box_list[i]
        for j in range(i+1, N) : # 기준 원소 오른쪽에 있는 원소를 하나씩 순회하면서
            if base_box > box_list[j] : # 기준 원소보다 작은 원소의 개수를 하나씩 추가한다
                count += 1
        count_list += [count]

     # 낙차 중에서 가장 큰 낙차를 구한다
    
    max_count = count_list[0]
    for i in range(N) :  # len(count_list) 대신 N 을 사용한다 ㅡ len() 사용 자제
        if max_count < count_list[i] :
            max_count = count_list[i]
           
    print(f'#{test_case} {max_count}')