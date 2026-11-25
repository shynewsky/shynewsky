S = input()
for alphabet in 'abcdefghijklmnopqrstuvwxyz':
    print(S.index(alphabet) if alphabet in S else -1, end=' ')
