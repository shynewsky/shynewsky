from collections import Counter

str_list = Counter(input().upper()).most_common()

if len(str_list) == 1:
    print(str_list[0][0])
elif str_list[0][1] == str_list[1][1]:
    print('?')
else:
    print(str_list[0][0])
