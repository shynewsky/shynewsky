T = int(input())
for t in range(1, T+1):
    # 입력
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    count = 0
    for i in range(N-1): #기준점
        for j in range(i+1, N): #비교점
            A, B = matrix[i]
            a, b = matrix[j]
            if (A > a and b > B) or (a > A and B > b) :
                count += 1
                    
    print(f'#{t}',count)                    
        