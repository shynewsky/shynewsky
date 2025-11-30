import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):

    # 입력 ㅡ 뒤에 공백 strip() 해줘야한다
    arr = list(input().strip()) # 문자열을 리스트로 받아온다
    N = len(arr)

    # 회문 검사
    for i in range(N//2):
        if arr[i] != arr[N-1-i]:
            print(False)
            break
    else: # break 로 안 끝났으면
        print(True)
