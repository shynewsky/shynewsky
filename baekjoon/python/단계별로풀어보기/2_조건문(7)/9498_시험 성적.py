# 방1)

score = int(input())
if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')

# 방2)
# 'A' if score >= 90
# else 'B' if score >= 80
# else 'C' if score >= 70
# else 'D' if score >= 60
# else 'F'

print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F')
