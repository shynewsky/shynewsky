N = int(input()) # 과정횟수

def recur(cnt, dot):
    if cnt == N:
        print(dot ** 2)
        return
    recur(cnt+1, dot+(dot-1))

recur(0, 2)
