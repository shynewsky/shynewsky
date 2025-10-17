#import sys
#sys.stdin = open("input.txt", "r")

#T = int(input())
T = 10

for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))
    
    sum = 0 
    
    for i in range(2, N-2) : # 주변 빌딩 4개 구하기
        side_list = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]

        max_side = side_list[0]
        for side in side_list : 
            
            if max_side < side :
                max_side = side
        
        if max_side < arr[i] :
            sum += (arr[i] - max_side)
            
    print(f'#{test_case} {sum}')
            
            
            
            
            
            
            
            