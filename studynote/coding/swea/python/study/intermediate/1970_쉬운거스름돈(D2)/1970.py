import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1):

    # 입력
    N = int(input()) # 거슬러줘야하는 금액

    # 방1) 소인수분해와 비슷하다
    divide = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(divide)):

        while N // divide[i] != 0: # 몫이 0이 될때까지
            change[i] = N // divide[i] # 몫은 채워 넣는다
            N -= (change[i] * divide[i]) # 나머지는 다시 돌린다

    # 방2) divmod() 함수 활용
    # divmod() : 몫과 나머지를 튜플로 반환하는 함수

    divide1 = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change1 = []

    for i in divide1 :
        div, mod = divmod(N, i) # div 몫, mod 나머지
        change1.append(div) # 몫은 채워넣는다
        N = mod # 나머지는 다시 돌린다

    # 출력
    print(f'#{test_case}')
    print(' '.join([str(i) for i in change1])) # 문자열 리스트만 가능. 문자열로 변환

