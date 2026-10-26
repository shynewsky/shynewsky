while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == a2 == a3 == 0:
        break
    if a1+a2 <= a3\
        or a2+a3 <= a1\
        or a3+a1 <= a2:
        print('Invalid')
    elif a1 == a2 == a3:
        print('Equilateral')
    elif a1 == a2 != a3\
        or a2 == a3 != a1\
        or a3 == a1 != a2:
        print('Isosceles')
    elif a1 != a2 != a3:
        print('Scalene')
