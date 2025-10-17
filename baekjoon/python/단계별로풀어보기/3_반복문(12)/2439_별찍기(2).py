# 방1)

T = int(input())
for i in range(T):
    print(' ' * (T-i-1), end='')
    print('*' * (i+1))

# 방2) ㄱㅁㅈ님

N = int(input())
for i in range(1, N+1):
    star = '*'*i
    print(star.rjust(N))
