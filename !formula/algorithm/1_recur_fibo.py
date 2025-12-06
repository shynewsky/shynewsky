# 재귀함수
def fibo1(n):
    if n < 2 :
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)

#--------------------------------------------------

# 동적계획법 (재귀X)
# Bottom Up : 0을 호출해서 [0]부터 하나씩 채워나가는것
'''
dp[0] = 0
dp[1] = 1
dp[2] = dp[1] + dp[0] = 1
dp[3] = dp[2] + dp[1] = 2
dp[4] = dp[3] + dp[2] = 3
dp[5] = dp[4] + dp[3] = 5
'''
def fibo2(n):
    arr = [0] * (n+1)
    arr[0], arr[1] = 0, 1
    for i in range(2, n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

#--------------------------------------------------

# 메모이제이션 (재귀O)
# Top Down : 5를 호출한 다음에, 0까지 내려가서 [0]부터 하나씩 채워나가는것
'''
fib(5)
 └─ fib(4)
     └─ fib(3)
         └─ fib(2)
             ├─ fib(1) = 1
             └─ fib(0) = 0
             => fib(2) = 1
         └─ fib(1) = 1
         => fib(3) = 2
     └─ fib(2) (이미 메모에 있음 = 1)
     => fib(4) = 3
 └─ fib(3) (이미 메모에 있음 = 2)
 => fib(5) = 5
'''
n = 10
arr = [0] * (n + 1)
arr[0], arr[1] = 0, 1
def fibo3(n):
    if n >= 2 and arr[n] == 0: # 초기화상태일때
        arr[n] = fibo3(n-1) + fibo3(n-2)
    return arr[n]
