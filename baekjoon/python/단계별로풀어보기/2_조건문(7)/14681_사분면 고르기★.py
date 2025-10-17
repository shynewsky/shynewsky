x = int(input())
y = int(input())

# 방1)

if x > 0 :
    if y > 0 :
        print(1)
    else :
        print(4)
else :
    if y > 0 :
        print(2)
    else :
        print(3)

# 방2)
    # value = dict[key] ㅡ key 불변형 : 숫자, 문자, 불리언, 튜플
    # value = dict[1]
    # value = dict['1']
    # value = dict[True]
    # value = dict[(True, False)]

    # key1 = (x > 0)
    # key2 = (y > 0)
    # value = dict[(key1, key2)]

    # value = dict[(x > 0, y > 0)]

print({(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}[(x > 0, y > 0)])


