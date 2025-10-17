# 방1)

arr = list(map(int, input().split())) # [3, 3, 6]

if arr[0] == arr[1] == arr[2] : # 같은 눈 3개
    print(10000 + (arr[0] * 1000))

elif arr[0] == arr[1] != arr[2] : # 같은 눈 2개
    print(1000 + (arr[0] * 100))
elif arr[1] == arr[2] != arr[0] : # 같은 눈 2개
    print(1000 + (arr[1] * 100))
elif arr[2] == arr[0] != arr[1] : # 같은 눈 2개
    print(1000 + (arr[2] * 100))

elif arr[0] != arr[1] != arr[2] : # 다른 눈 2개
    print(max(arr) * 100)

# 방2)

a, b, c = sorted(map(int, input().split()))
print(10000 + a*1000 if a == c else 1000 + b*100 if a == b or b == c else 100*c)

# 방3)

from collections import Counter

arr = list(map(int, input().split()))
(num, cnt), = Counter(arr).most_common(1)  # 최빈값과 개수
print(10000 + num*1000 if cnt == 3 else 1000 + num*100 if cnt == 2 else max(arr)*100)




