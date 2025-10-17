import sys
sys.stdin = open('input.txt')

# 입력
T = 10
for t in range(1, T+1):
    N = int(input()) # 암호문 개수
    passwords = list(input().split()) # 암호문 뭉치
    M = int(input()) # 명령어 개수
    commands = list(input().split()) # 명령어
    # M != len(commands)

    # 코드
    idx = 0 # 명령어뭉치 위치
    while idx < len(commands):
        if commands[idx] == 'I':
            x = int(commands[idx+1])
            y = int(commands[idx+2])
            s = commands[idx+3:idx+3+y]
            passwords = passwords[:x] + s + passwords[x:]
            idx += 3 + y
        elif commands[idx] == 'D':
            x = int(commands[idx+1])
            y = int(commands[idx+2])
            passwords = passwords[:x] + passwords[x+y:]
            idx += 3
        elif commands[idx] == 'A':
            y = int(commands[idx+1])
            s = commands[idx+2:idx+2+y]
            passwords += s
            idx += 2 + y

    print(f'#{t}', *passwords[:10])