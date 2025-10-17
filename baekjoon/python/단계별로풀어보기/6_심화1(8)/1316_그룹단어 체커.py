import sys
sys.stdin = open('input.txt')

N = int(input())
str_list = list(input() for _ in range(N))
s = []
count = 0
for string in str_list:
    s.clear()
    for char in string:
        if len(s) == 0 : # 첫번째 글자는 바로 넣기
            s.append(char)
        elif (char in s) and (s[-1] != char): # 이어지지 않았는데 이미 있던 문자이면
            break
        else:
            s.append(char)
    else:
        count += 1

print(count)
