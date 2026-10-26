T = int(input()) # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    #개수가 정해진 다수의 정수를 입력받는 방법
    N, M = map(int, input().split()) 
    
    #개수가 정해지지 않은 다수의 정수를 입력받는 방법
    A = list(map(int, input().split())) 
    B = list(map(int, input().split()))
    
    #결과를 넣고 비교할 리스트를 하나 만든다
    C = list()
    
    #원래는 N이 큰 경우와, M이 큰 경우로 나누려고 했는데
    #ChatGPT 에서 N과 M을 비교해서, 더 큰 배열을 B로 지정한 게 더 괜찮아보인다

    if N>= M :
        N, M = M, N
        A, B = B, A
    
    for i in range(0, M-N+1) :
        sum = 0
        for j in range(0, N) : 
            sum += A[j] * B[i+j]
        C.append(sum)
    #C.sort()
    #print(f"#{test_case} {C[M-N]}")
    print(f"#{test_case} {max(C)}")