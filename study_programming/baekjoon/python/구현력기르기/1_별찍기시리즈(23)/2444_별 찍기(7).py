N = int(input())
for i in range(1, N):
    print(' ' * (N-i) + '*' * (2*i-1))
for i in range(N, -1, -1):
    print(' ' * (N-i) + '*' * (2*i-1))

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

# 방2)
for i in range(1-N, N, 1):
    print(' ' * abs(i) + '*' * abs(1- 2*N + 2*abs(i)))
