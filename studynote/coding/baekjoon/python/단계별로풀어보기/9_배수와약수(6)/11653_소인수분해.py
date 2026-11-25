N = int(input())
i = 2
while N // i != 0:
    if N % i == 0:
        N //= i
        print(i)
    else:
        i += 1