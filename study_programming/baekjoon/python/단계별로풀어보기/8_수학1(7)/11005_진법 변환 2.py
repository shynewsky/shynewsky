# 인덱스번호 = 10진법
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())

answer = ''
while N > 0 :
    remain = N % B
    N //= B
    answer = arr[remain] + answer

print(answer)
