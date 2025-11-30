import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 수

for test_case in range(1, T+1) :

    # 입력 받기
    N, M = map(int, input().split()) # N*N, 회문길이 M
    matrix = [list(input()) for _ in range(N)] # N행만큼 받아오기

    # 회문찾기
    # 회문은 한 보드당 하나씩 존재한다
    count = 0
    string = [0] * M  # 회문 알파벳을 넣기 위한 배열 만들기

    # 가로 회문 찾기
    for i in range(N) : # 기준점 행 이동
        for j in range(N-M+1) : # 기준점 열 이동 (가로 회문 길이만큼 줄이기)

            for k in range(M//2) : # 회문 길이만큼 확인하기
                if matrix[i][j + k] != matrix[i][j + (M-1-k)] : # k 랑 M-1-k 대응
                    break
            else : # break 없이 끝났으면 회문
                string = [matrix[i][j + k] for k in range(M)] # 회문 담기

    # 세로 회문 찾기
    for i in range(N-M+1) : # 기준점 행 이동 (세로 회문 길이만큼 줄이기)
        for j in range(N) : # 기준점 열 이동

            for k in range(M//2) : # 회문 길이만큼 확인하기
                if matrix[i+k][j] != matrix[i+(M-1-k)][j] : # k 랑 M-1-k 대응
                    break
            else : # break 없이 끝났으면 회문
                string = [matrix[i+k][j] for k in range(M)] # 회문 담기

    print(f'#{test_case}', ''.join(string))

