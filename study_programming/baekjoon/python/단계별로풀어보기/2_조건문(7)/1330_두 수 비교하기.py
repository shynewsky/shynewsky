# 방1)

A, B = map(int, input().split())
if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')

# 방2)
# if ㅡ '>' if A > B
# elif ㅡ else '<' if A < B
# else ㅡ else '=='

print('>' if A > B else '<' if A < B else '==')

