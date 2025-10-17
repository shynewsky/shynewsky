# 방1)

H, M = map(int, input().split())

if M - 45 >= 0 :
    print(H, M-45)
else :
    if H -1 >= 0 :
        print(H-1, M+60-45)
    else :
        print(H+24-1, M+60-45)

# 방2)

H = (H - 1) % 24 if M < 45 else H    # 단위가 24시간인 경우, %24 를 사용한다
M = (M - 45) % 60                    # 단위가 60분 인 경우, %60 을 사용한다
print(H, M)

# 방3)

print((H - (M < 45)) % 24, (M - 45) % 60)
