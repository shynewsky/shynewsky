while True:
    N = int(input())
    if N == -1:
        break
    factors = [i for i in range(1, N) if N % i == 0]
    if N == sum(factors):
        print(f"{N} = {' + '.join([str(i) for i in factors])}")
    else:
        print(f"{N} is NOT perfect.")
