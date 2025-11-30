T = int(input()) # 테스트케이스 수

for test_case in range(1, T+1) : 
    
    # 입력 받기
    arr = list(map(int, input().split()))
    N = len(arr)
    
    # 부분집합은 2^N 가지
    # 파이썬에서는 1<<2 가 2^N 와 같은 표현
    # 공집합을 제외하고 싶으므로, 1부터 시작
    for i in range(1, 1<<N) : # i 는 부분집합을 비트로 표현한 '마스크' 역할을 함
        set_sum = 0 
        
        for j in range(N) : # arr 안에서 몇번째 숫자인지
            if i & (1<<j) : # i의 j번째 자리가 1인지 확인 ㅡ 이 숫자를 고른 상태인지 확인
                set_sum += arr[j] # j번째 숫자를 고른 상태면, 합에 누적
        
        if set_sum == 0:
            print(1)
            break
    else :
        print(0)
