# top 사용

s2 = [0] * 3
top = -1

top += 1
s2[top] = 1

top += 1
s2[top] = 2

top += 1
s2[top] = 3

top -= 1
print(s2[top+1]) # 3

top -= 1
print(s2[top+1]) # 2

top -= 1
print(s2[top+1]) # 1

