# 방1)

a, b, c, d, e, f = map(int, input().split())
x = int((c*e - f*b)/(a*e - b*d))
y = int((c*d - a*f)/(b*d - a*e))
print(x, y)

# 방2)

a, b, c, d, e, f = map(int, input().split())
x = ((f*b) - (c*e)) // ((b*d) - (a*e))
y = ((c*d) - (f*a)) // ((b*d) - (a*e))
print(f'{x} {y}')
