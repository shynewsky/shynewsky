T = int(input())

for test_case in range(1, T+1) :
    
    # 입력받기
    arr = input()
    N = len(arr)
    
    # '(' 일때 stack 에 push
    # ')' 일때 stack 에서 pop()
    # ㄴ 이전 문자가 '(' 이면 레이저 - 현재 스택에 있는 막대들 수만큼 조각 생성
    # ㄴ 이전 문자가 ')' 이면 막대의 끝 - 하나의 막대가 끝났으므로 조각 1개 추가
    
    stack = [] 
    result = 0
    
    for i in range(N) : 

        if arr[i] == '(' :
            stack.append('(')
        else :
            stack.pop()
            
            if arr[i-1] == '(' : # 레이저인 경우
                result += len(stack)
            else : # 막대기의 끝인 경우
                result += 1
    
    print(f'#{test_case} {result}')